import pandas as pd

def clean_agent_data(txns, agents):

    # Make copies of the original data
    clean_txns = txns.copy()
    agent_register = agents.copy()

    # Create a cleaning log
    log = []

    # 1. Remove duplicate transactions
    duplicates = clean_txns["txn_id"].duplicated().sum()
    clean_txns = clean_txns.drop_duplicates(subset="txn_id")

    log.append(["Duplicate transactions removed", duplicates])

    # 2. Standardise transaction types
    clean_txns["txn_type"] = clean_txns["txn_type"].str.strip().str.title()

    # 3. Convert amounts to numbers
    clean_txns["amount"] = pd.to_numeric(
        clean_txns["amount"], errors="coerce"
    )

    # 4. Convert transaction dates to datetime
    clean_txns["txn_date"] = pd.to_datetime(
        clean_txns["txn_date"].astype("string").str.replace(
            "/", "-", regex=False
        ),
        errors="coerce"
    )

    # 5. Flag missing amounts
    clean_txns["amount_flag"] = clean_txns["amount"].isna()

    missing_amounts = clean_txns["amount_flag"].sum()
    log.append(["Missing amounts flagged", missing_amounts])

    # 6. Flag outliers using the IQR method
    Q1 = clean_txns["amount"].quantile(0.25)
    Q3 = clean_txns["amount"].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    clean_txns["outlier_flag"] = (
        (clean_txns["amount"] < lower_limit) |
        (clean_txns["amount"] > upper_limit)
    )

    outliers = clean_txns["outlier_flag"].sum()
    log.append(["Outliers flagged", outliers])

    # 7. Join transactions to the agent register
    clean_txns = clean_txns.merge(
        agent_register, on="agent_id", how="left", indicator=True
    )

    clean_txns["unknown_agent_flag"] = clean_txns["_merge"] == "left_only"

    unknown_agents = clean_txns["unknown_agent_flag"].sum()
    log.append(["Unknown agents flagged", unknown_agents])

    clean_txns = clean_txns.drop(columns=["_merge"])

    # Create the cleaning log table
    cleaning_log = pd.DataFrame(
        log, columns=["Cleaning step", "Number of rows"]
    )

    return clean_txns, cleaning_log
