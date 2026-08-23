# DBMS Study Notes: Normalization, Transactions & Concurrency Control

## 1. Relational Database Normalization

Normalization reduces data redundancy and eliminates update, insertion, and deletion anomalies.

### Functional Dependency (FD) Rules & Armstrong's Axioms

- **Reflexivity:** If $Y \subseteq X$, then $X \to Y$.
- **Augmentation:** If $X \to Y$, then $XZ \to YZ$.
- **Transitivity:** If $X \to Y$ and $Y \to Z$, then $X \to Z$.

### Normal Forms Hierarchy

1. **First Normal Form (1NF):**
   - All attribute values are atomic (no arrays, multi-valued attributes, or nested relations).

2. **Second Normal Form (2NF):**
   - Is in 1NF.
   - No partial dependency: No non-prime attribute depends on a proper subset of any candidate key.

3. **Third Normal Form (3NF):**
   - Is in 2NF.
   - No transitive dependency: For every non-trivial FD $X \to A$, either $X$ is a superkey or $A$ is a prime attribute.

4. **Boyce-Codd Normal Form (BCNF):**
   - Is in 3NF.
   - Strict rule: For every non-trivial FD $X \to A$, $X$ **must** be a superkey.

---

## 2. Transactions & ACID Properties

A transaction is a logical unit of database execution.

### ACID Properties

- **Atomicity:** All operations complete successfully or the entire transaction is rolled back ("All or Nothing").
- **Consistency:** Transaction preserves database invariants and constraints.
- **Isolation:** Concurrent execution yields states equivalent to a serial execution.
- **Durability:** Committed changes persist across system failures.

---

## 3. Concurrency Control Mechanisms

### Lock-Based Protocols & Two-Phase Locking (2PL)

1. **Shared (S) vs Exclusive (X) Locks:**
   - Multiple S locks allowed; X lock requires exclusive access.
2. **Strict Two-Phase Locking (Strict 2PL):**
   - **Growing Phase:** Transaction acquires locks but releases none.
   - **Shrinking Phase:** Transaction releases locks but acquires no new locks.
   - **Strict Rule:** All exclusive locks held by a transaction are released *only* when the transaction commits or aborts. Prevents cascading rollbacks.

### Deadlock Handling

- **Prevention:** Wait-Die (non-preemptive) vs Wound-Wait (preemptive) schemes using timestamps.
- **Detection:** Wait-For Graph (WFG) cycle detection.
