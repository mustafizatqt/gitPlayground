def dfs(curr,viz):
	for i in li[curr]:
		alp[s[i]-'a']+=1
		mx = max(mx,alp[s[i]-'a'])
		dfs(i,viz.add(i))
		alp[s[i]-'a']-=1

#this is a new commit extra comment!
	
