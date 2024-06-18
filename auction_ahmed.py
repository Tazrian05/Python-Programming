import random

import numpy as np


class User:
    """
    Represents a user in the auction.

    Attributes:
        __probability (float): Secret probability attribute to represent the probability of clicking on an ad.

    Methods:
        show_ad(): Returns True if the user clicks on an ad, False otherwise.
    """
    # using this technique from async video lecture
    def __init__(self):
        self.__probability = (
            np.random.uniform()
        )  

    def show_ad(self):
        """Returns True if the user clicks on an ad, False otherwise."""
        return np.random.choice(
            [True, False], p=[self.__probability, 1 - self.__probability]
        )


class Auction:
    def __init__(self, users, bidders):
        
        """
        Represents an auction.

        Attributes:
        users (list): List of User objects participating in the auction.
        bidders (list): List of Bidder objects participating in the auction.
        balances (dict): Dictionary to track the balances of bidders.
        user_ids (dict): Dictionary mapping User objects to their corresponding IDs.

        Methods:
        execute_round(): Executes one round of the auction.
        """
        self.users = users
        self.bidders = bidders
        self.balances = {bidder: 0 for bidder in bidders}
        self.user_ids = {users[i]: i for i in range(len(users))}

    def execute_round(self):
        """Executes one round of the auction."""
        chosen_user = random.choice(self.users)

        # bids will be a dictionary where the keys are bidder objects, and the values are the bids returned
        # by calling the bid() method on each bidder, using the user ID obtained from self.user_ids[chosen_user].
        bids = {
            bidder: bidder.bid(self.user_ids[chosen_user]) for bidder in self.bidders
        }

        # Sort bids in descending order
        sorted_bids = sorted(bids.values(), reverse=True)

        # Determine the winning bid (highest bid)
        winning_bid = sorted_bids[0]

        # Determine the second-highest bid
        second_highest_bid = sorted_bids[1] if len(sorted_bids) > 1 else sorted_bids[0]

        # Find the winning bidder(s) with the highest bid. This is a list comprehension that creates a list.
        # It iterates over all key-value pairs in bids, and for each pair, it checks if the bid is equal to the highest bid.
        # If it is, it includes the bidder (which is the key, representing a bidder object) in the list.
        winning_bidders = [bidder for bidder, bid in bids.items() if bid == winning_bid]

        # Randomly select one of the winning bidders
        winning_bidder = random.choice(winning_bidders)

        user_click = chosen_user.show_ad()

        for bidder in self.bidders:
            if bidder == winning_bidder:
                price = second_highest_bid  # Set the winning price to the second-highest bid
                clicked = user_click
                won_auction = True
                bidder.notify(won_auction, price, clicked)
                if clicked:
                    self.balances[bidder] += 1
                self.balances[bidder] -= price
            else:
                won_auction = False
                price = second_highest_bid
                bidder.notify(won_auction, price, None)
