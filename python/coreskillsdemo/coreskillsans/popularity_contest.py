def popularity_contest(name_list):
    cnt = Counter()
    for word in name_list:
        cnt[word] += 1
        t = word
    final = OrderedDict(sorted(cnt.items(), key=lambda t: t[0]))
    for key,word in final.items():
        print(key,"got",word,"votes.")
    print(t,"Wins!")