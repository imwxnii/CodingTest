sem = { "Algorithm":204, "DataAnalysis":207, "ArtificialIntelligence":302 ,"CyberSecurity":	"B101" ,"Network":	303 ,"Startup":	501, "TestStrategy":105}
n = int(input())
ls = []
for _ in range(n):
    x = input()
    ls.append(x)
for ss in ls:
    print(sem[ss])