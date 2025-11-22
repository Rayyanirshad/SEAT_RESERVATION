# --- Configuration (Easy Python Basics) ---
# Reservation grace period in "ticks" (actions taken by user/coordinator).
GRACE_PERIOD = 3 
TOTAL_SEATS = 10
CURRENT_USER_ID = "Student-101" 

# --- Global State ---
SEATS_DATA = []
CURRENT_TICK = 0 # Tracks elapsed time

def initialize_seats():
    """Initial setup of 10 seats."""
    global SEATS_DATA
    SEATS_DATA = []
    blocks = ['A', 'B']
    
    for block in blocks:
        for desk in range(1, 6): # A1-A5, B1-B5
            SEATS_DATA.append({
                'serial': f"{block}{desk}",
                'desk': desk,
                'table': f"T-{block}",
                'status': 'Available',  # Available or Reserved
                'reserved_by': None,
                'reserved_tick': None,
            })

def check_for_expired_seats():
    """Auto-unreserves seats if the grace period is over."""
    for seat in SEATS_DATA:
        if seat['status'] == 'Reserved' and seat['reserved_tick'] is not None:
            expiration_tick = seat['reserved_tick'] + GRACE_PERIOD
            
            if CURRENT_TICK >= expiration_tick:
                # Only auto-release if not reserved by the current session user
                if seat['reserved_by'] != CURRENT_USER_ID:
                    seat['status'] = 'Available'
                    seat['reserved_by'] = None
                    seat['reserved_tick'] = None
                    print(f"[ALERT] Seat {seat['serial']} auto-unreserved (expired).")
                else:
                     print(f"[NOTICE] Your reservation for {seat['serial']} has expired!")

def display_status_and_counts():
    """Prints seat status and calculates reserved/vacant totals."""
    check_for_expired_seats()
    
    reserved = 0
    available = 0
    
    print("\n" + "="*50)
    print("      Library Seat Status (Tick: {})".format(CURRENT_TICK))
    print("="*50)
    
    for seat in SEATS_DATA:
        status = seat['status']
        serial = seat['serial']
        time_info = ""
        
        if status == 'Reserved':
            reserved += 1
            remaining = GRACE_PERIOD - (CURRENT_TICK - seat['reserved_tick'])
            if remaining > 0:
                time_info = f" | Time left: {remaining} ticks"
            else:
                time_info = " | EXPIRED"

            reserved_info = "(YOU)" if seat['reserved_by'] == CURRENT_USER_ID else "(Other)"
            print(f"[{status:9}] {serial:<4} (Desk: {seat['desk']}){reserved_info}{time_info}")

        elif status == 'Available':
            available += 1
            print(f"[{status:9}] {serial:<4} (Desk: {seat['desk']})")
        
    print("="*50)
    print(f"SUMMARY: Reserved Seats: {reserved}")
    print(f"         Vacant Seats (Unreserved): {available}")
    print("="*50)
    
    return reserved, available

def get_seat(seat_id):
    """Helper to find a seat by serial."""
    return next((s for s in SEATS_DATA if s['serial'] == seat_id.upper()), None)

def student_reserve():
    """Book a seat by serial number."""
    if any(s['reserved_by'] == CURRENT_USER_ID and s['status'] == 'Reserved' for s in SEATS_DATA):
        print("Error: You already have an active reservation.")
        return

    seat_id = input("Enter seat Serial (e.g., A3) to BOOK: ")
    seat = get_seat(seat_id)
    
    if seat and seat['status'] == 'Available':
        seat['status'] = 'Reserved'
        seat['reserved_by'] = CURRENT_USER_ID
        seat['reserved_tick'] = CURRENT_TICK
        print(f"Success! Seat {seat['serial']} reserved. Must arrive within {GRACE_PERIOD} ticks.")
    elif seat:
        print(f"Error: Seat {seat['serial']} is {seat['status']}.")
    else:
        print("Error: Seat not found.")

def student_unreserve():
    """Manually unreserve my seat if I can't come."""
    seat_id = input("Enter YOUR reserved seat Serial to UNRESERVE: ")
    seat = get_seat(seat_id)
    
    if seat and seat['status'] == 'Reserved' and seat['reserved_by'] == CURRENT_USER_ID:
        seat['status'] = 'Available'
        seat['reserved_by'] = None
        seat['reserved_tick'] = None
        print(f"Success! Seat {seat['serial']} manually released.")
    else:
        print("Error: Seat is not reserved by you, or it's not reserved.")

def coordinator_check():
    """Coordinator views and acknowledges vacant seats."""
    print("\n--- Coordinator Update Panel ---")
    reserved, available = display_status_and_counts()

    # Coordinator updates / acknowledges
    input("\n[COORDINATOR ACTION] Press ENTER to acknowledge vacant seats ({}).".format(available))
    print(f"[LOG] Coordinator acknowledged. Reserved={reserved}, Vacant={available}")
    
    # Simple override option
    override = input("Manually set a seat AVAILABLE (Y/N)? ").upper()
    if override == 'Y':
        seat_id = input("Enter seat Serial to force AVAILABLE: ")
        seat = get_seat(seat_id)
        if seat:
            seat['status'] = 'Available'
            seat['reserved_by'] = None
            seat['reserved_tick'] = None
            print(f"Override Success: Seat {seat['serial']} is now Available.")
        else:
            print("Seat not found.")


def run_app():
    """Main application loop."""
    global CURRENT_TICK
    initialize_seats()
    print("College Library Seat System (Short CLI)")
    
    while True:
        display_status_and_counts()
        
        print("\n--- Menu ---")
        print("1. Reserve a Seat")
        print("2. Manually Unreserve My Seat")
        print("3. Coordinator Check/Update")
        print("4. Quit")

        choice = input("Select action (1-4): ")
        
        if choice == '1':
            student_reserve()
        elif choice == '2':
            student_unreserve()
        elif choice == '3':
            coordinator_check()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")
        
        # Time advances after every action
        CURRENT_TICK += 1

if __name__ == "__main__":
    run_app()

