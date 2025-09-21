# Project Requirements

## 1. Project Overview

Provide a brief description of the project, its purpose, and its scope.

**Example:**  
This project aims to develop an Automated Purchase Order Management System (OWSB) to streamline inventory management, track purchase orders, and generate stock reports.

---

## 2. Functional Requirements

List the main functionalities the system must provide. Use numbering or bullet points.

1. **Inventory Management**

   - View available items and stock levels.
   - Update stock automatically after approved purchase orders.
   - Alert low-stock items.

2. **Purchase Order Management**

   - Create, approve, and track purchase orders.
   - View details of each purchase order.
   - Generate reports of purchase order history.

3. **Reporting**

   - Generate stock reports in table format.
   - Generate summary reports of purchase orders.

4. **User Interface**
   - Tabs or sections for viewing items, updating stock, stock alerts, and reports.
   - Auto-load data when switching tabs (no buttons required).

---

## 3. Non-Functional Requirements

Specify quality attributes the system should meet.

- **Performance:** The system should handle up to X items and Y purchase orders without noticeable delay.
- **Usability:** User-friendly GUI with clear tables and labels.
- **Reliability:** Stock updates and alerts must be accurate and consistent.
- **Maintainability:** Code should follow modular design principles and be easy to update.

---

## 4. Constraints

State any limitations or conditions.

- The system will use file-based storage (text files) for persistence.
- Java Swing will be used for the GUI.
- The project must adhere to the UML diagrams specified in the design.

---

## 5. References

List references or documents used to define requirements.

- `DomainModel.md`
- `LogicalDesign.md`
- Project specifications provided by the instructor or client
