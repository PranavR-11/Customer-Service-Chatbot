import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_BOOK = """You can book a cab instantly from your cab App using RIDE NOW option 
           Follow these steps:-

	- Turn on your phone's Locations settings (Location or GPS) to make a booking,login to your Cab App. 
          On Logging in, you'll be shown cabs that are near your location.
	- Set up your pickup location and enter your drop location,select a cab type and then click RIDE NOW. 

	You will receive a booking confirmation on your App screen. You will be able to view your ride details, 
	cab location on the map, and the time your driver will take to pick you up on Pickup Arriving screen."""
R_BOOKLATER = """With Ride Later option on your Cab App, you can book a cab from your Cab app up to 7 days in        
                advance to 1hr 15 mins ahead of the desired pickup time.
	Follow these steps to prebook-
	- Login to your cab App and on Book your Ride screen enter the pickup location where you would like the 
	driver to pick you up,select a cab category and tap RIDE LATER option to make a booking.
	- Select Date and Time for your pickup and confirm your booking by clicking CONFIRM BOOKING button """
R_PLOC = """Please check that your phone’s GPS is switched ON. This allows the app to automatically select 
           your current location as the pickup address.
	You can perfect your pickup location by moving the location pin on the map to the location where 
	you want the cab to pick you up from or entering your location in the search bar on top of the screen. """
R_DLOC = """You can choose to enter drop location on Book your Ride screen to get fare estimate for your ride. 
            is done by entering the drop location in the search box provided on top of the screen or move the 
            location pin on the map to the location where you want the cab to drop you.
            During the trip, at any time, you can choose to change the drop location and your driver will be informed. """
R_TRACK = """Once your booking is confirmed, you will be able to track your cab. You will be able to see your cab’s 
             location on the map and also the time it will it take for the driver to pick you up.You can also 
             track your cab from Your Rides section in your cab app menu. All you need to do is to select your 
             upcoming ride and 	tap Track Ride option available on the screen. """
R_OTP = """Once your booking is confirmed, you will receive an OTP via push notification on your phone. 
           On boarding the cab, you will need to share the OTP with the driver to start the trip.
           You can also find the OTP for your ride on Track Ride screen.  """
R_PAY = """At the end of the ride, you can check your total ride bill on driver’s app screen. You will also be 
           informed about the bill amount through a push notification. You can Pick a payment option before 
           you confirm a booking from Cash, E- Money, Postpaid, Credit/Debit card to pay for your cab ride. 
           We request you to  pick the payment option carefully before you confirm the booking. Once your 
           booking is confirmed, you will not be able to change your payment option. """   
                   
def unknown():
    response = "I don't quite understand, would you like to talk to a real person instead? "
    return response
