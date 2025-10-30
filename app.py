# import streamlit
import streamlit as st

# Add snowflakes animation
st.markdown("""
<style>
.snowflake {
    color: #fff;
    font-size: 1em;
    font-family: Arial, sans-serif;
    text-shadow: 0 0 5px #000;
    position: fixed;
    top: -10%;
    z-index: 9999;
    user-select: none;
    cursor: default;
    animation-name: snowflakes-fall, snowflakes-shake;
    animation-duration: 10s, 3s;
    animation-timing-function: linear, ease-in-out;
    animation-iteration-count: infinite, infinite;
    animation-play-state: running, running;
}

@keyframes snowflakes-fall {
    0% {top: -10%;}
    100% {top: 100%;}
}

@keyframes snowflakes-shake {
    0%, 100% {transform: translateX(0);}
    50% {transform: translateX(80px);}
}

.snowflake:nth-of-type(0) {left: 1%; animation-delay: 0s, 0s;}
.snowflake:nth-of-type(1) {left: 10%; animation-delay: 1s, 1s;}
.snowflake:nth-of-type(2) {left: 20%; animation-delay: 6s, 0.5s;}
.snowflake:nth-of-type(3) {left: 30%; animation-delay: 4s, 2s;}
.snowflake:nth-of-type(4) {left: 40%; animation-delay: 2s, 2s;}
.snowflake:nth-of-type(5) {left: 50%; animation-delay: 8s, 3s;}
.snowflake:nth-of-type(6) {left: 60%; animation-delay: 6s, 2s;}
.snowflake:nth-of-type(7) {left: 70%; animation-delay: 2.5s, 1s;}
.snowflake:nth-of-type(8) {left: 80%; animation-delay: 1s, 0s;}
.snowflake:nth-of-type(9) {left: 90%; animation-delay: 3s, 1.5s;}
.snowflake:nth-of-type(10) {left: 25%; animation-delay: 2s, 0s;}
.snowflake:nth-of-type(11) {left: 65%; animation-delay: 4s, 2.5s;}
</style>

<div class="snowflake">❅</div>
<div class="snowflake">❆</div>
<div class="snowflake">❅</div>
<div class="snowflake">❆</div>
<div class="snowflake">❅</div>
<div class="snowflake">❆</div>
<div class="snowflake">❅</div>
<div class="snowflake">❆</div>
<div class="snowflake">❅</div>
<div class="snowflake">❆</div>
<div class="snowflake">❅</div>
<div class="snowflake">❆</div>
""", unsafe_allow_html=True)

# Title
st.title('Hi, I am Prathosh!')
st.image('https://media3.giphy.com/media/MPxg9U887PS0B8XT4J/200w.gif?cid=6c09b952fk1klredu0gun45htyicmpkul8oxiax7dnjr2j2h&ep=v1_gifs_search&rid=200w.gif&ct=g', width=300)

# Header
st.header('Welcome to my Page!')


# About Me section
st.markdown('### About Me:')
st.markdown('Welcome to my website! I am Prathosh, a passionate 5th grader with a deep love for Godzilla. Soccer is my favorite sport, and I have a quirky habit of constantly changing wallpapers, although I am not quite sure why! Feel free to explore and discover more about me and my interests here.')
st.markdown('---')


# My Interests section
st.markdown('### My Interests:')
st.markdown("As previously mentioned, I have a fondness for Godzilla. Drawing is one of my passions, and I have access to plenty of drawing materials because my mom is an artist. Additionally, I'm quite enthusiastic about playing soccer. It's a game I love dearly, and I make it a point to play it every day at school. Furthermore, I enjoy playing video games, particularly on my PlayStation5. Games like Lego Undercover are among my favorites. I also cherish the time spent playing with my friends. I have a sizable group of friends, and playing with them brings me immense joy. Moreover, I relish playing with my parents and my sister. I have a special affection for German Shepherds and puppies, although this doesn't mean I enjoy Paw Patrol; in fact, I strongly dislike it. I've been yearning to have a German Shepherd puppy named Muto for quite some time.")
st.image('https://i.pinimg.com/originals/2c/48/8f/2c488ff14973e572d4e20ced00220aca.gif', width=300)
st.markdown('---')

# My Hobbies section
st.markdown('### My Hobbies:')
st.markdown("""I have a strong passion for writing fantasy books, drawing inspiration from movies featuring nearly immortal monsters and beasts.
            Additionally, I'm a devoted fan of the Harry Potter series, finding great enjoyment in both reading and writing stories inspired by it.
            While playing video games is enjoyable for me, I wouldn't necessarily consider it a hobby due to time constraints.
            I find myself incredibly busy, primarily because of the significant amount of homework I have. 
            Nevertheless, I prefer this busy schedule over attending Challenger, a rigorous school.""") 
st.image('https://i.pinimg.com/originals/1a/af/16/1aaf162ed448874e6fe411356d029675.gif', width=300)
st.markdown('---')



# My Projects section
st.markdown('### My Projects:')
st.markdown("Coming soon...")
st.markdown('---')



# To test locally,
# bash run_app.

# To push to GitHub, run the following commands in the terminal:
# bash git_push. https://prathosh.streamlit.app/
