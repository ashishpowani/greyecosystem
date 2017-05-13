import mastodon 
import xlsxwriter
from mastodon  import Mastodon
import textblob
import nltk
import time


#language_translator = LanguageTranslator(
#   username='cfae4f65-e562-441e-9bca-f90751c59541',
#   password='fQqF7xiK1Mij')
   
   
# Register app - only once!


# Mastodon.create_app(
     # 'pytooterapp',
      # to_file = 'pytooter_clientcred.txt'
# )


# Log in - either every time, or use persisted

mastodon = Mastodon(client_id = 'pytooter_clientcred.txt')
mastodon.log_in(
    'imranshaik@mail.usf.edu',
    'imranshaik',
    to_file = 'pytooter_usercred.txt'
)


# # Create actual instance
mastodon = Mastodon(
    client_id = 'pytooter_clientcred.txt',
    access_token = 'pytooter_usercred.txt'
 )
#toot from python using the created app
#mastodon.toot('Tooting from python!')


#getting account details
mastodon.account('440e674a4af6971d4f2b94ec90d219398097012eb105b2b1745a5583980bf2a5')


workbook = xlsxwriter.Workbook('mastodondata.xlsx')
worksheet = workbook.add_worksheet()
row=0
col=0

#get public timelines
timelines =list()
for i in range(1,20):
	timelines.append(mastodon.timeline_public(max_id=None, since_id=None, limit=None))
	time.sleep(5)
	
#print('timeline',timelines)

post=timelines[0]
for key in post[0].keys():
	if (key != 'account' and key !='application' and key!='media_attachments' and key!='mentions' and key!='tags'):
		worksheet.write(row,col,key)
		col+=1

row+=1
col=0
badkeys=list()

for timeline in timelines:
	for posts in timeline:
		#account=posts['account']
		#application=posts['application']
			for key in posts:
				if (key != 'account' and key !='application' and key!='media_attachments' and key!='mentions' and key!='tags'):
					if type(posts[key])!='list' or type(posts[key])!='dict' or type(posts[key])!=None:
						value=posts[key]
						if key=='content':
							#posts[key]=posts[key][3:]
							#value=language_translator.translate(posts[key],source='ja', target='en')
							value="'"+str(value)+"'"
							worksheet.write(row,col,value)
						worksheet.write(row,col,value)
						#outputcsv.write(row,cal,value)
						col+=1
					else:
						value=''
						worksheet.write(row,col,value)
						#outputcsv.write(row,col,value)
						badkeys.append(key)
						col+=1
			row+=1
			col=0
	
	
	
workbook.close()
print('badkeys',badkeys)


#discovering attributes in post
#print(timeline_public[0])


