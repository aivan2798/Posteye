fb_app_url="www.facebook.com/v20.0/dialog/oauth?client_id=314957010159410&redirect_uri=https://posteye.herokuapp.com&state={3v3vry_thing_starts_with_1_4-15-20}&response_type=token"
#replace https://posteye.herokuapp.com with your website url
fb_redirect_url="https://posteye.herokuapp.com"
#fb_redirect_url="https://127.0.0.1:5000"

fb_test_post="1028442447224794_2319430228126003"

SENTIMENTS=19980
EMOTIONS=20140
BEHAVIORS=20170
SENTIMENT_FILTER=199801
EMOTIONS_FILTER=201401
BEHAVIORS_FILTER=201701

ANALYZE_POST=24645
FILTER_COMMENTS=24646

CMD_REDIR=19000
CMD_TICK=19010
CMD_LOGOUT=19020
#permissions="user_posts,pages_manage_cta,pages_show_list,pages_read_user_content,pages_manage_engagement,public_profile,pages_read_engagement"
permissions="pages_show_list,pages_read_user_content,pages_manage_engagement"
