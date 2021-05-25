
urls_list = ['https://www.linkedin.com/sales/people/ACwAABDE45MBm3a6PfK80mSCDJglaHlBllgq2WY,NAME_SEARCH,Qgvr',
			 'https://www.linkedin.com/sales/people/ACwAAAtuG68BOUSl986wCDFS-CSqsULDlLAqWec,NAME_SEARCH,Tcq1'] 


link_list = []

for link in urls_list:
	new_link =link.replace('sales/people', 'in')
	new_link1= new_link[:-17]
	link_list.append(new_link1)
	print(link_list)
