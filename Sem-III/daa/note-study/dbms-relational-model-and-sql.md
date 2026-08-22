# DBMS Study Notes: ER Modeling, Relational Algebra & Advanced SQL

## 1. Entity-Relationship (ER) Modeling

An ER Model models real-world database systems structurally using entities, attributes, and relationships.

### Component Taxonomy

- **Entities:** Weak Entity Sets (depend on identifying entity via identifying relationship) vs Strong Entity Sets.
- **Attributes:** Simple, Composite, Single-valued, Multi-valued (double ellipse), Derived (dashed ellipse).
- **Mapping Cardinalities:** One-to-One (1:1), One-to-Many (1:N), Many-to-One (N:1), Many-to-Many (M:N).

---

## 2. Relational Algebra Operations

Relational algebra is a procedural query language consisting of fundamental operators.

### Fundamental Operators

1. **Selection ($\sigma_p(R)$):** Selects tuples matching predicate $p$.
2. **Projection ($\pi_{A_1, \dots, A_k}(R)$):** Selects specified columns and eliminates duplicate rows.
3. **Cartesian Product ($R \times S$):** Combines every tuple of $R$ with every tuple of $S$.
4. **Union ($R \cup S$):** Tuples in $R$ or $S$ ($R$ and $S$ must be union-compatible).
5. **Set Difference ($R - S$):** Tuples in $R$ but not in $S$.
6. **Rename ($\rho_{S(A_1, \dots, A_n)}(R)$):** Renames relation $R$ to $S$.

### Derived Operators

- **Natural Join ($R \bowtie S$):** Joins tuples matching on common attribute names.
- **Theta Join ($R \bowtie_{\theta} S$):** $\sigma_{\theta}(R \times S)$.
- **Division ($R \div S$):** Finds tuples in $R$ associated with *all* tuples in $S$.

---

## 3. Advanced SQL Querying

### Joins Summary

```sql
-- Inner Join
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- Left Outer Join (Retains un-matched left table rows)
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;
```

### Aggregation & Grouping Filter

```sql
SELECT dept_id, AVG(salary) AS avg_sal
FROM employees
WHERE status = 'ACTIVE'
GROUP BY dept_id
HAVING AVG(salary) > 75000;
```

### Subqueries & Window Functions

```sql
-- Correlated Subquery
SELECT name, salary, dept_id
FROM employees e1
WHERE salary > (
  SELECT AVG(salary)
  FROM employees e2
  WHERE e2.dept_id = e1.dept_id
);

-- Window Function (Ranking within partitions)
SELECT name, dept_id, salary,
       DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as dept_rank
FROM employees;
```
