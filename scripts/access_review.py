import pandas as pd

# Load the fictional employee access data
data = pd.read_csv("data/user_access_data.csv")

print("====================================")
print("     IT ACCESS CONTROL AUDIT")
print("====================================")

# Check for inactive accounts
inactive = data[data["Account_Status"] == "Inactive"]

print("\n1. INACTIVE ACCOUNTS")
print("-------------------")
print(inactive[["Employee_ID", "Employee", "Department"]])

# Check administrator privileges
admins = data[data["Admin_Privilege"] == "Yes"]

print("\n2. ADMINISTRATOR ACCOUNTS")
print("------------------------")
print(admins[["Employee_ID", "Employee", "Role"]])

# Check users without MFA
no_mfa = data[data["MFA_Enabled"] == "No"]

print("\n3. USERS WITHOUT MFA")
print("--------------------")
print(no_mfa[["Employee_ID", "Employee", "Department"]])

# Display audit summary
print("\n4. AUDIT SUMMARY")
print("----------------")
print("Total users:", len(data))
print("Inactive accounts:", len(inactive))
print("Administrator accounts:", len(admins))
print("Users without MFA:", len(no_mfa))
