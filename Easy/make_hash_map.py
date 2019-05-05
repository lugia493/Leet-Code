'''
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
'''

'''
We use arrays for direct access table
We use linked list for a chaining hash map
'''

class ListNode:
    def __init__(self, key, value):
        self.pair = (key, val)
        self.next = None

class MyHashMap(object):

    def __init__(self):
        # Define the size of the hash table size
        self.m = 1000
        # Define the hash map as an array
        self.h = [None] * self.m

    def put(self, key,value):
        # Since our hash map is finite size.
        # we need to mod the key by the size
        # to get an index in between 0 - size 
        # of table
        index = key % self.m

        # if the h array at index is None, 
        # then at the index of the array,
        # make it point to a new node consisting
        # of key and value
        if self.h[index] == None:
            self.h[index] = ListNode(key,value)
        else:
            # if there is a ListNode at index, there is collusion
            # we need to append the new value to end of the linked
            # list or update the value if key exisits in the 
            # linked list
            curr = self.h[index]
            # Traverse the linked list
            while True:
                # if there is a node whos key is the same
                # as another nodes key in the linked list
                # update the value and return
                if curr.pair[0] == key:
                    curr.pair = (key, value)
                    return
                # if we traverse, and find the end of 
                # the linked list, we will place the new node
                # there. So we break out of the while loop
                if curr.next == None:
                    break
                # iterate through the list nodes
                curr = curr.next
            # At this point, if we havnt returned,
            # curr.next points to None. So set the 
            # new node.
            curr.next = ListNode(key,value)

    def get(self, key):
        # We get the hash table index
        # from the key 
        index = key % self.m

        # We get the curr pointer from
        # the hash table at the index
        curr = self.h[index]

        # We will traverse the linked list at 
        # the index in the hash table until 
        # curr is None, or at the end of LL
        while curr:
            # if we find the key in the LL 
            # then we return the value
            if curr.pair[0] == key:
                return curr.pair[1]
            # Otherwise, we iterate through
            # the linked list
            else:
                curr = curr.next
        # If we reach None at the 
        # linked list, then we cant
        # find the node. Return -1
        return -1

    def remove(self,key):
        # Get the index
        index = key % self.m

        # Set curr, prev to the pointer
        # at the index of hash table
        curr = prev = self.h[index]

        # if the pointer is None
        # at the index we are looking at
        # then just return
        if not curr:
            return
        
        # if the ListNode at the index in 
        # the hash map is the key,
        # then we need to set the index
        # to the curr next value, which
        # could be None or could be another 
        # linked list
        if curr.pair[0] == key:
            self.h[index] = curr.next
        # Otherwise, there is a linked list
        # here, and we must traverse the linked
        # list
        else:
            # increment the curr. By doing this
            # prev point the the old curr, 
            # as we have updated to new curr now
            curr = curr.next
            # loop while curr is not None
            while curr:
                # if we find the key we are looking for
                # then have the previous node point
                # to the curr next node. This effectively
                # eliminates the node we were looking to 
                # remove. Then break out of while loop
                if curr.pair[0] == key:
                    prev.next = curr.next
                    break
                else:
                    # remember that because prev equals
                    # old curr and curr is new curr, 
                    # we could just have both of them 
                    # traverse the linked lists
                    curr, prev = curr.next, prev.next


