import tempfile

LOGIN_DATA = "utf8=✓&authenticity_token={authenticity_token}&user[email]={email}&user[password]={password}&user[remember_me]=0,1"
LOGIN_URL = "https://www.datacamp.com/users/sign_in"
LOGIN_DETAILS_URL = "https://www.datacamp.com/api/users/signed_in"

SESSION_FILE = tempfile.gettempdir() + "/.datacamp"

PROFILE_URL = "https://www.datacamp.com/profile/{slug}"
COURSE_DETAILS_API = "https://campus-api.datacamp.com/api/courses/{id}/"
EXERCISE_DETAILS_API = "https://campus-api.datacamp.com/api/exercise/{id}"