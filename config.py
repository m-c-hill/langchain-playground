from dotenv import load_dotenv

import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PROXY_CURL_API_KEY = os.getenv("PROXY_CURL_API_KEY")
PROXY_CURL_LINKEDIN_API_URL = "https://nubela.co/proxycurl/api/v2/linkedin"
LINKEDIN_PROFILE_URL = "https://www.linkedin.com/in/m-c-hill"


INFORMATION = """
Haruki Murakami (Japanese: 村上 春樹) is a popular contemporary Japanese writer and translator. His work has been described as 'easily accessible, yet profoundly complex'. He can be located on Facebook at: https://www.facebook.com/harukimuraka...

Since childhood, Murakami has been heavily influenced by Western culture, particularly Western music and literature. He grew up reading a range of works by American writers, such as Kurt Vonnegut and Richard Brautigan, and he is often distinguished from other Japanese writers by his Western influences.

Murakami studied drama at Waseda University in Tokyo, where he met his wife, Yoko. His first job was at a record store, which is where one of his main characters, Toru Watanabe in Norwegian Wood, works. Shortly before finishing his studies, Murakami opened the coffeehouse 'Peter Cat' which was a jazz bar in the evening in Kokubunji, Tokyo with his wife.

Many of his novels have themes and titles that invoke classical music, such as the three books making up The Wind-Up Bird Chronicle: The Thieving Magpie (after Rossini's opera), Bird as Prophet (after a piano piece by Robert Schumann usually known in English as The Prophet Bird), and The Bird-Catcher (a character in Mozart's opera The Magic Flute). Some of his novels take their titles from songs: Dance, Dance, Dance (after The Dells' song, although it is widely thought it was titled after the Beach Boys tune), Norwegian Wood (after The Beatles' song) and South of the Border, West of the Sun (the first part being the title of a song by Nat King Cole).
"""
