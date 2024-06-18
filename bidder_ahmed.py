import random


class Bidder:
    """
    Represents a bidder in the auction.

    Attributes:
        num_users (range): Range of user IDs.
        num_rounds (int): Number of rounds in the auction.
        __bid_history (dict): Dictionary to store bid history for each user.
        __epsilon (float): Exploration parameter for epsilon-greedy strategy.
        __balance (int): Current balance of the bidder.
        __bid_for_user (int): User ID for which the bidder is making a bid.

    Methods:
        bid(user_id): Makes a bid for a specific user ID.
        notify(auction_winner, price, clicked): Notifies the bidder about the auction result.
    """
    
    def __init__(self, num_users, num_rounds):
        self.num_users = range(num_users)
        self.num_rounds = num_rounds
        self.__bid_history = {} 
        self.__epsilon = 0.01 
        self.__balance = 0 
        self.__bid_for_user = None

    def bid(self, user_id):
        """
        Makes a bid for a specific user ID.

        Args:
            user_id (int): ID of the user for which the bid is made.
        Returns:
            float: The bid amount.
        """
        
        if user_id not in self.__bid_history:
            self.__bid_history[user_id] = []
        bid_amount = 0  # default value for bid amount

        # Using epsilon greedy strategy
        if random.random() < self.__epsilon:
            bid_amount = round(random.uniform(0, 1), 3)
        else:
            if self.__bid_history[user_id]:
                bid_amount = max(
                    self.__bid_history[user_id]
                )    # choose the highest bid from bid history
        self.__bid_for_user = user_id
        return bid_amount

    def notify(self, auction_winner, price, clicked):        
        """
        Notifies the bidder about the auction result.

        Args:
            auction_winner (bool): True if the bidder won the auction, False otherwise.
            price (float): Amount the bidder pays if they won.
            clicked (bool): True if the user clicked on the ad, False otherwise.
        """

        if auction_winner:
            if clicked:
                self.__balance += 1  # Increase balance by 1
            self.__balance -= price  # decrease balance by bid price

        if self.__bid_for_user not in self.__bid_history:
            self.__bid_history[self.__bid_for_user] = []

        self.__bid_history[self.__bid_for_user].append(price)
