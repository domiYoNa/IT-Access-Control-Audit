# IT Access Control Audit Report

## 1. Executive Summary

This project presents a simulated IT Access Control Audit for a fictional organization.

The audit reviewed employee account status, administrative privileges, and Multi-Factor Authentication (MFA).

The analysis identified potential control weaknesses involving inactive accounts, privileged access, and missing MFA.

All data used in this project is fictional and created for educational purposes.

---

## 2. Audit Objective

The objective of this audit is to assess whether basic user access controls are operating appropriately and to identify potential access-control risks.

---

## 3. Audit Scope

The audit reviewed the following areas:

- Employee account status
- Administrative privileges
- Multi-Factor Authentication (MFA)
- Potential access-control risks

---

## 4. Audit Methodology

The audit was performed using the following steps:

1. Reviewed fictional employee access data.
2. Identified inactive accounts.
3. Identified accounts with administrative privileges.
4. Identified users without MFA.
5. Analyzed the results using Python.
6. Documented potential control weaknesses.
7. Provided recommended remediation actions.

---

## 5. Audit Evidence

The dataset contained:

- 10 total user accounts
- 2 inactive accounts
- 2 administrator accounts
- 3 accounts without MFA

The analysis was performed using Python and the pandas library.

---

## 6. Audit Findings

### Finding 1 — Inactive User Accounts

**Risk Rating: High**

Two inactive accounts were identified:

- EMP005 — David
- EMP010 — Lina

**Potential Risk:**

Inactive accounts may retain access to organizational systems if the account lifecycle process is not followed.

**Recommendation:**

The organization should disable accounts promptly when employees leave or become inactive. Periodic user-access reviews should also be performed.

---

### Finding 2 — Administrative Privileges

**Risk Rating: Medium**

Two accounts have administrative privileges:

- EMP002 — Rahul — System Administrator
- EMP006 — Sara — Developer

The developer account should be reviewed to determine whether administrative access is required for the user's job responsibilities.

**Potential Risk:**

Excessive privileges can increase the impact of unauthorized access or account compromise.

**Recommendation:**

The organization should apply the principle of least privilege and periodically review privileged accounts.

---

### Finding 3 — Users Without MFA

**Risk Rating: High**

Three accounts do not have MFA enabled:

- EMP005 — David
- EMP007 — Alex
- EMP010 — Lina

**Potential Risk:**

Accounts protected only by passwords may have increased exposure to unauthorized access.

**Recommendation:**

MFA should be enabled for all applicable accounts, with priority given to privileged and sensitive accounts.

---

## 7. Control Testing Summary

| Control Area | Test Performed | Result |
|---|---|---|
| Account Lifecycle | Checked inactive accounts | Potential Weakness |
| Privileged Access | Reviewed administrator accounts | Requires Review |
| MFA | Checked MFA status | Potential Weakness |

---

## 8. Risk Summary

| Finding | Risk | Priority |
|---|---|---|
| Inactive Accounts | Unauthorized access | High |
| Administrative Privileges | Excessive access | Medium |
| Missing MFA | Account compromise | High |

---

## 9. Recommendations

The organization should:

1. Disable inactive accounts promptly.
2. Perform periodic user-access reviews.
3. Review all administrative privileges.
4. Apply least-privilege principles.
5. Enable MFA for applicable accounts.
6. Maintain evidence of access reviews and remediation.

---

## 10. Conclusion

The simulated audit identified potential weaknesses in account lifecycle management, privileged access, and MFA controls.

The project demonstrates a basic Technology Audit workflow:

**Evidence → Control Testing → Risk Identification → Findings → Recommendations**

This project uses fictional data and is intended for educational and portfolio purposes.
