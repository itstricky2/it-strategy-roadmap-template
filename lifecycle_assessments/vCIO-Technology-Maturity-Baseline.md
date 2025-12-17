# vCIO Technology Maturity Baseline

> **Timing**: At onboarding, then annually
> **Purpose**: Establish a defensible baseline and measure progress objectively over time

---

## 1. Identity & Access Management

**1. Is MFA enforced for all users and administrators?**
- [ ] Yes, everywhere
- [ ] Partial (Admins only / Remote only)
- [ ] No
- [ ] Unknown

**2. Are privileged accounts clearly identified and limited?**
- [ ] Yes (Separate admin accounts used)
- [ ] No (Admins use daily driver accounts)
- [ ] Unknown

**3. Is user access reviewed periodically?**
- [ ] Yes (quarterly/annually)
- [ ] No (only upon termination)

---

## 2. Endpoint & Patch Management

**4. Are all endpoints centrally managed (MDM/RMM)?**
- [ ] Yes (100% coverage)
- [ ] Partial
- [ ] No

**5. Is patching automated and monitored?**
- [ ] Yes
- [ ] No (manual or user-driven)

**6. Are unsupported operating systems in use?**
- [ ] No
- [ ] Yes (List count/reason): ______________

---

## 3. Backup & Recovery

**7. Are backups tested on a scheduled basis?**
- [ ] Yes (Automated verification + Periodic restore tests)
- [ ] Automated verification only
- [ ] No
- [ ] Unsure

**8. Are backups immutable or otherwise protected from ransomware?**
- [ ] Yes (Air-gapped / Immutable cloud)
- [ ] No (Accessible via standard creds)
- [ ] Unsure

**9. Are RTO (Recovery Time) and RPO (Recovery Point) defined and achievable?**
- [ ] Defined and tested
- [ ] Defined but untested
- [ ] Not defined

---

## 4. Network Architecture

**10. Is the network segmented by function or risk?**
- [ ] Yes (VLANs/Zones for Guest, IoT, Corp, Server)
- [ ] Partial
- [ ] Flat network (Everything talks to everything)

**11. Are guest, IoT, and operational systems isolated?**
- [ ] Yes
- [ ] No

**12. Is remote access centrally controlled and logged?**
- [ ] Yes (VPN/ZTNA with MFA)
- [ ] No (Open RDP/TeamViewer/etc)

---

## 5. Documentation & Process

**13. Are network diagrams current?**
- [ ] Yes (<6 months old)
- [ ] Outdated
- [ ] Non-existent

**14. Are critical procedures documented?**
- [ ] Yes (Standard Operating Procedures exist)
- [ ] No (Tribal knowledge)

**15. Could another team realistically recover systems if key staff were unavailable?**
- [ ] Yes
- [ ] Doubtful
- [ ] No

---
*Date: __________________*
*Assessor: __________________*
