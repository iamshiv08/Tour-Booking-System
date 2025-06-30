import streamlit as st
import re

# Tour Packages
tour_packages = {
    "Ahmedabad": {
        "description": "Ahmedabad is a vibrant city known for its rich history, cultural heritage, and delicious Gujarati cuisine",
        "price": 10000,
        "hotel": "Taj Skyline (5⭐) - offering modern amenities, exquisite dining options, and elegant accommodations, set in the heart of the city, ideal for both business and leisure travelers",
        "available_dates": [
            "2025-04-15",
            "2025-05-01",
            "2025-05-15",
            "2025-06-01",
            "2025-06-15",
            "2025-07-01",
            "2025-07-15",
            "2025-08-01",
        ],
        "days": 5,
    },
    "Surat": {
        "description": "Surat is a bustling commercial hub famous for its textile industry, vibrant diamond trade, and beautiful riverfront",
        "price": 8000,
        "hotel": "The Grand Bhagwati Surat (4⭐) - luxurious hotel offering elegant accommodations, fine dining, and top-notch services for both business and leisure travelers",
        "available_dates": [
            "2025-04-20",
            "2025-05-05",
            "2025-05-20",
            "2025-06-05",
            "2025-06-20",
            "2025-07-05",
            "2025-07-20",
            "2025-08-05",
        ],
        "days": 4,
    },
    "Mumbai": {
        "description": "Mumbai is a dynamic metropolis, known as the financial capital of India, famous for its bustling streets, Bollywood industry, and iconic landmarks like the Gateway of India",
        "price": 12500,
        "hotel": "The Taj Mahal Palace (5⭐) - historic luxury hotel offering world-class service, stunning views of the Arabian Sea, and iconic architectural beauty",
        "available_dates": [
            "2025-04-05",
            "2025-04-20",
            "2025-05-05",
            "2025-05-20",
            "2025-06-05",
            "2025-06-20",
            "2025-07-05",
            "2025-07-20",
        ],
        "days": 4,
    },
    "Goa": {
        "description": "Goa is a tropical paradise known for its pristine beaches, vibrant nightlife, Portuguese-influenced architecture, and laid-back vibe",
        "price": 12000,
        "hotel": "Taj Exotica Resort & Spa (5⭐) - an upscale beachfront resort offering luxurious stays, world-class amenities, and rejuvenating spa experiences",
        "available_dates": [
            "2025-04-08",
            "2025-04-22",
            "2025-05-08",
            "2025-05-22",
            "2025-06-08",
            "2025-06-22",
            "2025-07-08",
            "2025-07-22",
        ],
        "days": 7,
    },
    "Kerala": {
        "description": "Kerala is known for its stunning backwaters, beautiful beaches, rich cultural traditions, and lush greenery, offering a perfect mix of nature and tranquility",
        "price": 15000,
        "hotel": "Kumarakom Lake Resort (5⭐) - an exquisite resort offering luxurious stays with beautiful views of Vembanad Lake, traditional Kerala architecture, and world-class amenities",
        "available_dates": [
            "2025-04-10",
            "2025-04-25",
            "2025-05-05",
            "2025-05-20",
            "2025-06-05",
            "2025-06-20",
            "2025-07-10",
            "2025-07-25",
        ],
        "days": 9,
    },
}

# Main function
def main():
    menu = ["Tour Packages", "Book Packages", "View Booking"]
    st.sidebar.markdown(
        """<h1 style="font-size=50px">BookMyTrip 🚗</h1>""", unsafe_allow_html=True
    )
    st.sidebar.text(
        "BookMyTrip offers a seamless platform to easily book tour packages, providing a hassle-free and personalized travel booking experience"
    )
    choice = st.sidebar.selectbox("Menu", menu) 
    st.title("BookMyTrip 🚗")
    if choice == "Tour Packages":
        st.subheader("Available Tour Packages")
        for tour, details in tour_packages.items():
            st.markdown(
                f"""
                <div style="background-color: #333; padding: 20px; margin-bottom: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                    <h4 style="color: #FFFFFF;">{tour}</h4>
                    <p><strong>Description:</strong> {details['description']}</p>
                    <p><strong>Price:</strong> {details['price']}</p>
                    <p><strong>Hotel:</strong> {details['hotel']}</p>
                    <p><strong>Available Dates:</strong> {', '.join(details['available_dates'])}</p>
                    <p><strong>Days:</strong> {(details['days'])}</p>
                </div>
            """,
                unsafe_allow_html=True,
            )
    elif choice == "Book Packages":
        st.subheader("Book a Tour")
        tour_choice = st.selectbox("Choose a tour package", list(tour_packages.keys()))
        selected_tour = tour_packages[ tour_choice ]  # Gives that package details for the choice
        st.write(f"**Description**: {selected_tour['description']}")
        st.write(f"**Hotel**: {selected_tour['hotel']}")
        st.write(f"**Price per person**: {selected_tour['price']}")
        date_choice = st.selectbox("Choose a date", selected_tour["available_dates"])
        num_people = st.number_input(
            "Number of people", min_value=1, step=1, max_value=10
        )
        people_details = []
        for i in range(num_people):
            name = st.text_input(f"Name of Person {i+1}")
            age = st.number_input(
                f"Age of Person {i+1}", min_value=1, step=1, max_value=100
            )
            gender = st.radio(
                f"Gender of Person {i+1}", ["Male", "Female"], key=f"gender_{i}"
            )
            email = st.text_input(f"Email for Person {i+1}")
            if not name:
                st.error(f"Please fill the input box for Person {i+1}.")
                return
            if email and not re.match("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", email):
                st.error(f"Please fill valid Email for Person {i+1}.")
                return
            if not re.match("^[A-Za-z ]+$", name):
                st.error(
                    f"Invalid name for Person {i+1}. Only letters and spaces are allowed."
                )
                return
            people_details.append({"name": name, "age": age, "gender": gender, "email": email})
        total_price = selected_tour["price"] * num_people
        old_price = total_price
        dis = total_price * 0.10
        if total_price >= 50000:
            total_price = total_price - dis
            st.text(f"Total Price : {old_price}")
            st.success("10% Discount Applied")
        st.write(f"**Total Price for {num_people} person(s)**: {total_price}")

        if st.button("Proceed to Payment"):
            st.session_state["proceed_to_payment"] = True

        if st.session_state.get("proceed_to_payment", False):
            payment_type = st.selectbox("Select Payment Type", ["Debit Card", "UPI"])
            if payment_type == "Debit Card":
                card_number = st.text_input("Enter 12-digit Debit Card Number")
                cvv = st.text_input("Enter 3-digit CVV")
                if st.button("Pay Now"):
                    if len(card_number) != 12 or not card_number.isdigit():
                        st.error(
                            "Invalid Debit Card Number. Please enter a 12-digit number."
                        )
                    elif len(cvv) != 3 or not cvv.isdigit():
                        st.error("Invalid CVV. Please enter a 3-digit number.")
                    else:
                        st.success("Payment Successful! Your booking is confirmed.")
                        st.session_state["package_name"] = tour_choice
                        st.session_state["bookings"] = people_details
                        st.session_state["selected_tour"] = selected_tour
                        st.session_state["date_choice"] = date_choice
                        st.session_state["total_price"] = total_price
                        st.session_state["payment_details"] = {
                            "type": "Debit Card",
                            "card_number": card_number,
                            "cvv": cvv,
                        }
                        st.session_state["proceed_to_payment"] = False  # Reset payment state
            elif payment_type == "UPI":
                upi_id = st.text_input("Enter UPI Number")
                upi_pin = st.text_input("Enter UPI Pin")
                if st.button("Pay Now"):
                    if len(upi_id) != 10 or not upi_id.isdigit():
                        st.error("Invalid UPI ID. Please enter 10 Digit valid UPI ID.")
                    elif len(upi_pin) != 4 or not upi_pin.isdigit():
                        st.error("Invalid PIN. Please enter a 4-digit number.")
                    else:
                        st.success("Payment Successful! Your booking is confirmed.")
                        st.session_state["package_name"] = tour_choice
                        st.session_state["bookings"] = people_details
                        st.session_state["selected_tour"] = selected_tour
                        st.session_state["date_choice"] = date_choice
                        st.session_state["total_price"] = total_price
                        st.session_state["payment_details"] = {
                            "type": "UPI",
                            "upi_id": upi_id,
                        }
                        st.session_state["proceed_to_payment"] = False  # Reset payment state

    elif choice == "View Booking":
        st.subheader("My Bookings")

        if "bookings" in st.session_state:
            # Group the overall booking information in a container
            with st.container():
                st.markdown(
                    "<h3 style='color: #4CAF50;'>Booking Details</h3>",
                    unsafe_allow_html=True,
                )
            st.markdown(
                f"""
            <div style="background-color: #333; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                <p style="color: #FFFFFF; font-size: 18px;"><strong>Package Name:</strong> {st.session_state["package_name"]}</p>
                <p style="color: #FFFFFF; font-size: 16px;"><strong>Description:</strong> {st.session_state["selected_tour"]["description"]}</p>
                <p style="color: #FFFFFF; font-size: 16px;"><strong>Hotel:</strong> {st.session_state["selected_tour"]["hotel"]}</p>
                <p style="color: #FFFFFF; font-size: 16px;"><strong>Date:</strong> {st.session_state["date_choice"]}</p>
                <p style="color: #FFFFFF; font-size: 16px;"><strong>Total Price:</strong> {st.session_state["total_price"]}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
            # Display Traveler Information
            st.markdown(
                "<h3 style='color: #4CAF50;'>Traveler Details</h3>",
                unsafe_allow_html=True,
            )

            for i, booking in enumerate(st.session_state["bookings"], start=1):
                st.markdown(
                    f"""
                    <div style="background-color:#333; padding: 15px; border-radius: 10px; margin-bottom: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                        <h4 style="color: #F5F5F5 ; font-size: 20px;">Person {i}</h4>
                        <p style="color:#FFFFFF"><strong>Name:</strong> {booking['name']}</p>
                        <p style="color:#FFFFFF"><strong>Age:</strong> {booking['age']}</p>
                        <p style="color:#FFFFFF"><strong>Gender:</strong> {booking['gender']}</p>
                        <p style="color:#FFFFFF"><strong>Email:</strong> {booking['email']}</p>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

            # Display Payment Information
            if "payment_details" in st.session_state:
                st.markdown(
                    "<h3 style='color: #4CAF50;'>Payment Details</h3>",
                    unsafe_allow_html=True,
                )

                payment_details = st.session_state["payment_details"]
                if payment_details["type"] == "Debit Card":
                    st.markdown(
                        f"""
                        <div style="background-color:#333; padding: 15px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                            <p style="color:#FFFFFF"><strong>Payment Type:</strong> {payment_details['type']}</p>
                            <p style="color:#FFFFFF"><strong>Card Number:</strong> **** **** **** {payment_details['card_number'][-4:]}</p>
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )
                elif payment_details["type"] == "UPI":
                    st.markdown(
                        f"""
                        <div style="background-color:#333; padding: 15px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                            <p style="color:#FFFFFF"><strong>Payment Type:</strong> {payment_details['type']}</p>
                            <p style="color:#FFFFFF"><strong>UPI ID:</strong> {payment_details['upi_id']}</p>
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )
        else:
            st.write("No bookings found.")


if __name__ == "__main__":
    main()  
