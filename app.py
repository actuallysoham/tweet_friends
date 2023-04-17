import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from datetime import date, datetime

st.title('Twitter Friend Recommender')


def load_data(filename):
    data = pd.read_excel('recommendations/'+str(filename)+'.xlsx')
    return data




today = date.today()

data_1 = load_data('day1')
data_2 = load_data('day2')
data_3 = load_data('day3')
data_4 = load_data('day4')
data_5 = load_data('day5')
data_6 = load_data('day6')
data_7 = load_data('day7')
#st.write(data)

# username input: TODO - fix lowercase
username_input = st.text_input('Enter your Twitter username')

df = pd.read_csv('ashoka_users.csv')
select_users = list(df['username'])

if username_input in select_users:
	st.write('Congrats, you are part of the study')
	#reccs = list(data[data['username'] == username_input])
	reccs_1 = list(data_1.loc[data_1['username'] == username_input].values[0][2:])
	reccs_2 = list(data_2.loc[data_2['username'] == username_input].values[0][2:])
	reccs_3 = list(data_3.loc[data_3['username'] == username_input].values[0][2:])
	reccs_4 = list(data_4.loc[data_4['username'] == username_input].values[0][2:])
	reccs_5 = list(data_5.loc[data_5['username'] == username_input].values[0][2:])
	reccs_6 = list(data_6.loc[data_6['username'] == username_input].values[0][2:])
	reccs_7 = list(data_7.loc[data_7['username'] == username_input].values[0][2:])
	#print(reccs)
	

	tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Post Survey"])
	with tab1:
		if today >= datetime.strptime('2023-04-17',"%Y-%m-%d").date():
			st.header("Day 1")
			st.write("Here are 5 users we recommend you follow:")
			st.write("---")
			html_str = f"""
					<ol>
					<li><a href='https://twitter.com/{reccs_1[0]}'>twitter.com/{reccs_1[0]}</a></li>
					<li><a href='https://twitter.com/{reccs_1[1]}'>twitter.com/{reccs_1[1]}</a></li>
					<li><a href='https://twitter.com/{reccs_1[2]}'>twitter.com/{reccs_1[2]}</a></li>
					<li><a href='https://twitter.com/{reccs_1[3]}'>twitter.com/{reccs_1[3]}</a></li>
					<li><a href='https://twitter.com/{reccs_1[4]}'>twitter.com/{reccs_1[4]}</a></li>
					</ol>
					"""

			st.markdown(html_str, unsafe_allow_html=True)
			st.write("---")
			st.write("That's it for today! See you tomorrow :)")
		else:
			st.write("This page will be active after 2023-04-17")

	with tab2:

		if today >= datetime.strptime('2023-04-18',"%Y-%m-%d").date():
			st.header("Day 2")
			st.write("Here are 5 users we recommend you follow:")
			st.write("---")
			html_str = f"""
					<ol>
					<li><a href='https://twitter.com/{reccs_2[0]}'>twitter.com/{reccs_2[0]}</a></li>
					<li><a href='https://twitter.com/{reccs_2[1]}'>twitter.com/{reccs_2[1]}</a></li>
					<li><a href='https://twitter.com/{reccs_2[2]}'>twitter.com/{reccs_2[2]}</a></li>
					<li><a href='https://twitter.com/{reccs_2[3]}'>twitter.com/{reccs_2[3]}</a></li>
					<li><a href='https://twitter.com/{reccs_2[4]}'>twitter.com/{reccs_2[4]}</a></li>
					</ol>
					"""

			st.markdown(html_str, unsafe_allow_html=True)
			st.write("---")
			st.text("Please fill the survey to complete today's task:")
			st.markdown(f'''<a href='https://forms.gle/HBHD2mw9xZm1Hk1C8'>Link to Survey (Day 1)</a>''',unsafe_allow_html=True)

		else:
			st.write("This page will be active on and after 2023-04-18")
	   

	with tab3:

		if today >= datetime.strptime('2023-04-19',"%Y-%m-%d").date():
			st.header("Day 3")
			st.write("Here are 5 users we recommend you follow:")
			st.write("---")
			html_str = f"""
					<ol>
					<li><a href='https://twitter.com/{reccs_3[0]}'>twitter.com/{reccs_3[0]}</a></li>
					<li><a href='https://twitter.com/{reccs_3[1]}'>twitter.com/{reccs_3[1]}</a></li>
					<li><a href='https://twitter.com/{reccs_3[2]}'>twitter.com/{reccs_3[2]}</a></li>
					<li><a href='https://twitter.com/{reccs_3[3]}'>twitter.com/{reccs_3[3]}</a></li>
					<li><a href='https://twitter.com/{reccs_3[4]}'>twitter.com/{reccs_3[4]}</a></li>
					</ol>
					"""

			st.markdown(html_str, unsafe_allow_html=True)
			st.write("---")
			st.text("Please fill the survey to complete today's task:")
			st.markdown(f'''<a href='https://forms.gle/tRUooAD53k35X8Pq8'>Link to Survey (Day 2)</a>''',unsafe_allow_html=True)

		else:
			st.write("This page will be active on and after 2023-04-19")

	with tab4:

		if today >= datetime.strptime('2023-04-20',"%Y-%m-%d").date():
			st.header("Day 4")
			st.write("Here are 5 users we recommend you follow:")
			st.write("---")
			html_str = f"""
					<ol>
					<li><a href='https://twitter.com/{reccs_4[0]}'>twitter.com/{reccs_4[0]}</a></li>
					<li><a href='https://twitter.com/{reccs_4[1]}'>twitter.com/{reccs_4[1]}</a></li>
					<li><a href='https://twitter.com/{reccs_4[2]}'>twitter.com/{reccs_4[2]}</a></li>
					<li><a href='https://twitter.com/{reccs_4[3]}'>twitter.com/{reccs_4[3]}</a></li>
					<li><a href='https://twitter.com/{reccs_4[4]}'>twitter.com/{reccs_4[4]}</a></li>
					</ol>
					"""

			st.markdown(html_str, unsafe_allow_html=True)
			st.write("---")
			st.write("Please fill the survey to complete today's task:")
			st.markdown(f'''<a href='https://forms.gle/qDeb1Y6Mx7QS9UHn8'>Link to Survey (Day 3)</a>''',unsafe_allow_html=True)

		else:
			st.write("This page will be active on and after 2023-04-20")


	with tab5:

		if today >= datetime.strptime('2023-04-21',"%Y-%m-%d").date():
			st.header("Day 5")
			st.write("Here are 5 users we recommend you follow:")
			st.write("---")
			html_str = f"""
					<ol>
					<li><a href='https://twitter.com/{reccs_5[0]}'>twitter.com/{reccs_5[0]}</a></li>
					<li><a href='https://twitter.com/{reccs_5[1]}'>twitter.com/{reccs_5[1]}</a></li>
					<li><a href='https://twitter.com/{reccs_5[2]}'>twitter.com/{reccs_5[2]}</a></li>
					<li><a href='https://twitter.com/{reccs_5[3]}'>twitter.com/{reccs_5[3]}</a></li>
					<li><a href='https://twitter.com/{reccs_5[4]}'>twitter.com/{reccs_5[4]}</a></li>
					</ol>
					"""

			st.markdown(html_str, unsafe_allow_html=True)
			st.write("---")
			st.write("Please fill the survey to complete today's task:")
			st.markdown(f'''<a href='https://forms.gle/ZmmDHXMAgomjMJyY7'>Link to Survey (Day 4)</a>''',unsafe_allow_html=True)

		else:
			st.write("This page will be active on and after 2023-04-21")

	   
	with tab6:

		if today >= datetime.strptime('2023-04-22',"%Y-%m-%d").date():
			st.header("Day 6")
			st.write("Here are 5 users we recommend you follow:")
			st.write("---")
			html_str = f"""
					<ol>
					<li><a href='https://twitter.com/{reccs_6[0]}'>twitter.com/{reccs_6[0]}</a></li>
					<li><a href='https://twitter.com/{reccs_6[1]}'>twitter.com/{reccs_6[1]}</a></li>
					<li><a href='https://twitter.com/{reccs_6[2]}'>twitter.com/{reccs_6[2]}</a></li>
					<li><a href='https://twitter.com/{reccs_6[3]}'>twitter.com/{reccs_6[3]}</a></li>
					<li><a href='https://twitter.com/{reccs_6[4]}'>twitter.com/{reccs_6[4]}</a></li>
					</ol>
					"""

			st.markdown(html_str, unsafe_allow_html=True)
			st.write("---")
			st.write("Please fill the survey to complete today's task:")
			st.markdown(f'''<a href='https://forms.gle/aQiHnVYVwAxWTgcr9'>Link to Survey (Day 5)</a>''',unsafe_allow_html=True)

		else:
			st.write("This page will be active on and after 2023-04-22")


	with tab7:


		if today >= datetime.strptime('2023-04-23',"%Y-%m-%d").date():
			st.header("Day 7")
			st.write("Here are 5 users we recommend you follow:")
			st.write("---")
			html_str = f"""
					<ol>
					<li><a href='https://twitter.com/{reccs_7[0]}'>twitter.com/{reccs_7[0]}</a></li>
					<li><a href='https://twitter.com/{reccs_7[1]}'>twitter.com/{reccs_7[1]}</a></li>
					<li><a href='https://twitter.com/{reccs_7[2]}'>twitter.com/{reccs_7[2]}</a></li>
					<li><a href='https://twitter.com/{reccs_7[3]}'>twitter.com/{reccs_7[3]}</a></li>
					<li><a href='https://twitter.com/{reccs_7[4]}'>twitter.com/{reccs_7[4]}</a></li>
					</ol>
					"""

			st.markdown(html_str, unsafe_allow_html=True)
			st.write("---")
			st.write("Please fill the survey to complete today's task:")
			st.markdown(f'''<a href='https://forms.gle/pQFte4tmCof2tmYj9'>Link to Survey (Day 6)</a>''',unsafe_allow_html=True)

		else:
			st.write("This page will be active on and after 2023-04-23")

	with tab8:
		st.header("Post Survey")
		st.write("The link to the post survey will be shared after completion of all earlier tasks.")


elif len(username_input)>1 and username_input not in select_users:
	st.write('Sorry, you are not a part of this study')





