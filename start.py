"""Script to send auto replies to Birthday wishes on your facebook wall."""
import sys
import json
import random
import requests

REPLIES = ['Thanks ;)', 'Thank you so much :D', 'Thanx :)', 'Thanks a bunch!',
           'Thanks for making my day special! :)', 'Thanks so much. Hope you are doing great :)',
           'Thanks a ton!', 'Thank you my dear!', 'many many thanks :) :D']

TOKEN = "your fb token"

def get_birthday_posts():
    """Get all the Birthday posts from your wall"""
    init_url = 'https://graph.facebook.com/me/feed?access_token=' + TOKEN
    flag = True
    while flag:
        result = json.loads((requests.get(init_url)).text)
        # print result
        for i in range(0, len(result['data'])):
            if result['data'][i].has_key("message"):
                print result['data'][i]['from']['name'] + " : " + result['data'][i]['message']
                print "(R)eply, (n)ext or (e)xit?"
                user_response = str(raw_input())
                if user_response == 'R' or user_response == 'r':
                    # comment
                    comment = REPLIES[random.randint(0, len(REPLIES)-1)]
                    print "Replying With : " + comment

                elif user_response == 'n' or user_response == "N":
                    print "Skipping this guy"
                elif user_response == "e" or user_response == "E":
                    print "Exiting"
                    flag = False
                    break
                else:
                    print "No valid input"
            # get next set of data
            init_url = result['paging']['next']

def send_comment(post, comment):
    """Send your reply as comment to a particular post"""
    print "Replying With : " + comment
    requests.post("https://graph.facebook.com/" + post.split("_")[1] + "/comments?access_token="
                  + TOKEN + "&message=" + comment)

    #like
    res = requests.post("https://graph.facebook.com/" + post.split("_")[1] + "/likes?access_token="
                        + TOKEN)
    print res

def main():
    """Main entry point for the script."""
    get_birthday_posts()

if __name__ == '__main__':
    sys.exit(main())
