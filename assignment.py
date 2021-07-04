import sys
import math
import os
class IPL:
    PlayerTeam = []
    edges = [[],[]]
    franchises_names=[]
    player_names = []
	
    def __init__(self):
        self.PlayerTeam = []
        self.edges =[[],[]]
	
#function to read input file and display number of franchise, count of unique player, name of all franchise and name of unique player    
    def readInputFile(self, filename):
        try:
            f=open(filename,'r')
            playerList = []
            playernames = set()
            for line in f.readlines():
                line = line.replace('\n', '')
                data = line.split('/')
                self.franchises_names.append(data[0].strip())
                player_names = [datum.strip() for datum in data[1:]]
                playerList.append(player_names)
                playernames.update(set(player_names))
                self.player_names = list(playernames)
                self.player_names.sort()
            f.close()     
    		
            #print(self.franchises)
            #print(self.players)
            num_nodes = len(self.franchises_names) + len(self.player_names)
            self.edges = [[0]*num_nodes for i in range(num_nodes)]
            print(self.edges)
            for index, franchise in enumerate(self.franchises_names):
                for player in playerList[index]:
                    #print(player,index)
                    j = self.player_names.index(player)
                    #print(player,franchise,index,j+len(self.franchises))
                    self.edges[index][j+len(self.franchises_names)] =1
                    self.edges[j+len(self.franchises_names)][index]=1
            #print(len(self.edges[0]))
            #print(self.edges)
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise            
    
    def displayAll(self):
        s='--------Function displayAll--------'
        s+='\nTotal no. of franchises: '+str(len(self.franchises_names))
        s+='\nTotal no. of Players: '+str(len(self.player_names))
        s+='\n'
        s+='\nList of franchises: \n'
        s+="\n".join(self.franchises_names)
        s+='\n'
        s+='\nList of Players: \n'
        s+="\n".join(self.player_names)
        #print('\nList of players: ')
        #print("\n".join(self.players))
        print(s)
        return s

    def displayFranchises(self,player):
        printstring=''
        try:
            printstring+='\n--------Function displayFranchises --------'
            printstring+='\nPlayer name: '+player
            printstring+='\nList of Franchises: '
            if not self.player_names.__contains__(player):
                printstring+='\nPlayer not found'
            else:
                playerIndex = self.player_names.index(player) + len(self.franchises_names)
                found = False
                for i in range(len(self.franchises_names)):
                    if self.edges[playerIndex][i] == 1:
                        found = True
                        printstring+='\n'+self.franchises_names[i] + ' '
                if not found:
                    printstring+='\nPlayer not associated with any franchise '
            printstring+='\n-------------------------------------------'
            print(printstring)
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return printstring    
	
    def displayPlayers(self,franchise):
        printstring=''
        try:
            printstring+='\n--------Function displayPlayers --------'
            printstring+='\nFranchise name: '+franchise
            if not self.franchises_names.__contains__(franchise):
                printstring+='\nFranchise not found'
            else:
                franchiseIndex = self.franchises_names.index(franchise)
                found = False
                for i in range(len(self.player_names)):
                    j = i+len(self.franchises_names)
                    if self.edges[franchiseIndex][j] == 1:
                        found = True
                        printstring+='\n'+self.player_names[i]+' '
                if not found:
                    printstring+='\nFranchise not associated with any player '
            printstring+='\n-------------------------------------------'
            print(printstring)
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return printstring         
	
	
    def franchiseBuddies(self,playerA,playerB):
        printstring=''
        try:
            p1=self.player_names.index(playerA) + len(self.franchises_names)
            p2=self.player_names.index(playerB) + len(self.franchises_names)
            printstring+='\n--------Function franchiseBuddies --------'
            printstring+='\nPlayer A: '+playerA
            printstring+='\nPlayer B: '+playerB
            printstring+='\nFranchise Buddies: '
            found = False
            for i in range(len(self.franchises_names)):
                if self.edges[p1][i] == 1 and self.edges[p2][i] == 1:
                    found = True
                    printstring+='Yes, '+self.franchises_names[i]
            if not found:
                printstring+='\nNo, the players are not franchise buddies'
            printstring+='\n-------------------------------------------'
            print(printstring)    
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return printstring
	
    def printPath(self,nodes, parent, i):
        returnstring=''
        try:
            if parent[i] == -1:
            #print('*',i)
                returnstring+=nodes[i]+' > '
                return returnstring
            returnstring+= self.printPath(nodes, parent, parent[i])
        #print(i)
        #print(nodes[i])
            returnstring+=nodes[i]+' > '
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return returnstring    
	
    def findPlayerConnect(self, playerA, playerB):
        printstring=''
        try:
            printstring+='\n--------Function findPlayerConnect -------'
            printstring+='\nPlayer A: '+playerA
            printstring+='\nPlayer B: '+playerB
            p1 = len(self.franchises_names) + self.player_names.index(playerA)
            p2 = len(self.franchises_names) + self.player_names.index(playerB)
            #print(p1,p2)
            parent, dist = self.dijkstra(p1)
            #print(parent,dist)
            nodes = self.franchises_names
            nodes.extend(self.player_names)
            #print(nodes)
            if dist[p2] == 99999:
                printstring+='\nRelated: No'
            else:
                printstring+= '\nRelated: Yes, '
                printstring+= self.printPath(nodes, parent, p2)
            printstring+='\n-------------------------------------------'
            print(printstring)
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return printstring

    def MinimumPath(self,dist, visited):
    	minsize = math.inf
        #print('---------------')
        #print(dist)
        #print(minsize)
    	for i in range(len(dist)):
    		if dist[i] < minsize and visited[i] == False:
    			minsize = dist[i]
    			min_index = i
    	return min_index

    def dijkstra(self,src):
        adj=self.edges
        pathLength = [99999] * len(adj)
        pathLength[src] = 0
        vertexList = [False] * len(adj)
        predecesor = [-1] * len(adj)
        #print('**************')
        #print (visited)
        #print (parent)
        #print(dist)	
        for i in range(len(adj)):
            current_vertex = self.MinimumPath(pathLength, vertexList)
            #print(current_vertex)
            vertexList[current_vertex] = True
            for v in range(len(adj)):
                #print(v)
                #print(adj)
                #print(current_vertex,v,adj[current_vertex][v],vertexList[v],pathLength[v],pathLength[current_vertex])
                if adj[current_vertex][v] !=0 and vertexList[v] == False and pathLength[v] > pathLength[current_vertex] + adj[current_vertex][v]:
                    #print('---------------------------------------visited {0}{1} : ',current_vertex,v)
                    pathLength[v] = pathLength[current_vertex] + adj[current_vertex][v]
                    #print(pathLength[v],pathLength[current_vertex],adj[current_vertex][v])
                    predecesor[v] = current_vertex
        #print(predecesor)
        #print(pathLength)
        return predecesor, pathLength        

if __name__ == '__main__':
    try:
        i=IPL()
        inputfilename ="inputPS28.txt"
        outputfilename="outputPS28.txt"
        promptfilename="promptsPS28.txt"

#display Total Player, Total Franchise,Player Name , Franchise Name    
        i.readInputFile(inputfilename)
        if os.path.exists(outputfilename):
            os.remove(outputfilename)
        s=i.displayAll()
        outputfilehandler= open(outputfilename,'w')
        outputfilehandler.write(s)
        outputfilehandler.close()

#display Franchise of Player        
        promptfilehandler= open(promptfilename,'r')
        playername=[]
        for inputlines in promptfilehandler.readlines():
            #print('****************')
            inputlines = inputlines.replace('\n', '')
            inputlines=inputlines.strip()
            if(inputlines.split(':')[0].strip()=='findFranchise'):
                if(inputlines.split(':')[1].strip()!=''):
                    playername.append(inputlines.split(':')[1].strip())
        outputfilehandler.close()

        if(len(playername)==0):
            print('No player name found in Prompt file')
        else:
            for player in playername:
                s1=i.displayFranchises(player)
                outputfilehandler= open(outputfilename,'a+')
                outputfilehandler.write('\r\n'+s1)
                outputfilehandler.close()

#display past and current player of given Franchise                  
        promptfilehandler= open(promptfilename,'r')
        franchisename=[]
        for inputlines in promptfilehandler.readlines():
            #print('****************')
            inputlines = inputlines.replace('\n', '')
            inputlines=inputlines.strip()
            if(inputlines.split(':')[0].strip()=='listPlayers'):
                if(inputlines.split(':')[1].strip()!=''):
                    franchisename.append(inputlines.split(':')[1].strip())
        outputfilehandler.close()
        
        if(len(franchisename)==0):
            print('No franchise name found in Prompt file')
        else:
            for franchise in franchisename:
                s1=i.displayPlayers(franchise)
                outputfilehandler= open(outputfilename,'a+')
                outputfilehandler.write('\r\n'+s1)
                outputfilehandler.close()
                
#display franchise buddies                  
        promptfilehandler= open(promptfilename,'r')
        franchiseBuddies_set=[]
        for inputlines in promptfilehandler.readlines():            
            #print('****************')
            #franchiseBuddies=[]
            inputlines = inputlines.replace('\n', '')
            inputlines=inputlines.strip()
            #print(inputlines)
            if(inputlines.split(':')[0].strip()=='franchiseBuddies'):
                SetofBuddies=inputlines.split(':')[1:]
                #print('----->',SetofBuddies)
                if(len(SetofBuddies)==2):
                    if(SetofBuddies[0].strip()!='' and SetofBuddies[1].strip()!=''):
                        franchiseBuddies_set.append(SetofBuddies)
            
                    
        #print(franchiseBuddies_set)            
        outputfilehandler.close()
        #print(franchiseBuddies_set)
        if(len(franchiseBuddies_set)==0):
            print('No franchise buddies found in Prompt file')
        else:
            for franchise in franchiseBuddies_set:
                #print(franchise[0],franchise[1])
                s2=i.franchiseBuddies(franchise[0].strip(),franchise[1].strip())
                outputfilehandler= open(outputfilename,'a+')
                outputfilehandler.write('\r\n'+s2)
                outputfilehandler.close()

#display Player connect                  
        promptfilehandler= open(promptfilename,'r')
        playerconnect_set=[]
        for inputlines in promptfilehandler.readlines():            
            #print('****************')
            #franchiseBuddies=[]
            inputlines = inputlines.replace('\n', '')
            inputlines=inputlines.strip()
            #print(inputlines)
            if(inputlines.split(':')[0].strip()=='playerConnect'):
                Setofplayer=inputlines.split(':')[1:]
                #print('----->',SetofBuddies)
                if(len(Setofplayer)==2):
                    if(Setofplayer[0].strip()!='' and Setofplayer[1].strip()!=''):
                        playerconnect_set.append(Setofplayer)
            
                    
        #print(franchiseBuddies_set)            
        outputfilehandler.close()
        #print(franchiseBuddies_set)
        if(len(playerconnect_set)==0):
            print('No franchise buddies found in Prompt file')
        else:
            for playerA_B in playerconnect_set:
                #print(franchise[0],franchise[1])
                s3=i.findPlayerConnect(playerA_B[0].strip(),playerA_B[1].strip())
                outputfilehandler= open(outputfilename,'a+')
                outputfilehandler.write('\r\n'+s3)
                outputfilehandler.close()                
        
        
#        i.franchiseBuddies('Krunal Pandya','Kieron Pollard')
#        i.findPlayerConnect('Kedar Jadhav','Ishan Kishan')	
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])