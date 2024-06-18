def count_retweets_by_username(tweets):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """    
    # write code here and update return statement with your dictionary
    string_tweet=''.join(tweets)
    string_to_list=string_tweet.split()
    username=[]
    for item in string_to_list:
        if '@' in item:
            username.append(item[1:-1])
            
    username_dictionary={}
    for item in username:
        if item in username_dictionary:
            username_dictionary[item]+=1
        else:
            username_dictionary[item]=1
    return username_dictionary


def display(deposits, top, bottom, left, right):
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""
    
    grid = [['-'] * (right - left) for _ in range(bottom - top)] #creating grid to display based on input rows and columns
    
    for deposit in range(len(deposits)):
        deposits[deposit] = list(deposits[deposit]) #converting the tuples inside the list to lists
        if top <= deposits[deposit][0] < bottom and left <= deposits[deposit][1] < right: #checking row and column values from deposits within the input row and column range
            grid[deposits[deposit][0] - top][deposits[deposit][1] - left] = 'X' #updating grid with X
            
    # Generating the result string
    result = '\n'.join([''.join(row) for row in grid])
    return result



def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""
    
    grid = [['-'] * (right - left) for _ in range(bottom - top)] #creating grid to display based on input rows and columns
    sum=0
    for deposit in range(len(deposits)):
        deposits[deposit] = list(deposits[deposit]) #converting the tuples inside the list to lists
        if top <= deposits[deposit][0] < bottom and left <= deposits[deposit][1] < right: #checking row and column values from deposits within the input row and column range
            sum=sum+deposits[deposit][2]
    return sum



def birthday_count(dates_list):

    unique_dates = set(dates_list) #creating a set og unique dates
    total_pairs = 0

    for date in unique_dates:
        count = dates_list.count(date)
        total_pairs += count * (count - 1) // 2 #calculating the number of pairs using the combination formula n*(n-1)/2

    return total_pairs