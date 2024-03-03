# Vehicle Rental System

## Overview

This project aims to create a user-friendly vehicle rental system, enabling owners to effortlessly manage their fleets and customers to seamlessly book vehicles. The simplified approach ensures quick implementation while still providing essential functionalities for effective fleet control and customer satisfaction.

## Classes

### 1. Vehicle

- **Attributes:**
  - Vehicle ID
  - Model
  - Year
  - Type
  - Availability status

- **Methods:**
  - `checkAvailability()`
  - `getVehicleInformation()`

### 2. Owner

- **Attributes:**
  - Owner ID
  - Name
  - Contact information

- **Methods:**
  - `addVehicleToFleet()`
  - `removeVehicleFromFleet()`
  - `viewFleetReports()`

### 3. Customer

- **Attributes:**
  - Customer ID
  - Name
  - Contact information

- **Methods:**
  - `makeReservation()`
  - `viewReservationHistory()`
  - `cancelReservation()`

### 4. Reservation

- **Attributes:**
  - Reservation ID
  - Customer ID
  - Vehicle ID
  - Start date
  - End date

- **Methods:**
  - `calculateReservationCost()`
  - `confirmReservation()`
  - `cancelReservation()`

### 5. Rental System

- **Attributes:**
  - List of vehicles
  - List of owners
  - List of customers
  - List of reservations

- **Methods:**
  - `startSystem()`
  - `endSystem()`
  - `generateReports()`

## Features

1. **Fleet Management:**
   - Owners can add/remove vehicles to their fleet.
   - Check availability of vehicles.

2. **Reservations:**
   - Customers can make reservations for specific dates.
   - Reservation confirmation system.

3. **Reports:**
   - Owners can view reports on fleet usage.
   - Customers can access reservation history and costs.

4. **Usability:**
   - User-friendly interface for owners and customers.
   - Streamlined reservation process.

5. **Access Control:**
   - Secure authentication for owners and customers.
   - Role-based access restrictions.

---

*Note: This is a basic example in Markdown format. You can adapt and expand it as needed to meet the specific requirements of the project.*
