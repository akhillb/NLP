    data = line.split()
    if data[len(data)-1][0:4] == "http":
	link = data[len(data)-1]
	query = ""
	for i in range(1,len(data)-4):
	    query = query + data[i] + " "
	query = query.strip(" ")
	if not query_dict.has_key( query ):
	    url = []
	    url.append(link)
	    query_dict[query] = url
	    query_index[query] = qi
	    print query + " " + str(qi)
	    qj = qi
	    qi = qi + 1
	else:
	    if link not in query_dict[query]:
		query_dict[query].append( link )
	    qj = query_index[query]
	if not url_dict.has_key( link ):
	    q = []
	    q.append(query)
	    url_dict[link] = q
	    url_index[link] = ui
	    print link + " " + str(ui)
	    uj = ui
	    ui = ui + 1
	else:
	    if link not in query_dict[query]:
		url_dict[link].append( query )
	    uj = url_index[link]
	query_url = ( qj,uj )
	if count.has_key( query_url ):
	    count[query_url] = count[query_url] + 1
	else:
	    count[query_url] = 1


