#######################################################################
# Book Royalties Report using file : book.dat
# File:  book.py
# This is an example of processing data from different sequential files
#######################################################################

bookfile = open( "book.dat", mode = 'r' )

ta = 0                      # total author counter
tb = 0                      # total books accumulator
tr = 0.0                    # total royalties accumulator

#print headers
print("\n==============================================================")
print("                             BOOK ROYALTIES")
print("")
print("     NAME            TITLE               SOLD            DUE")
print("================================================================")
for authors in bookfile:
              authors = authors.split()
              name = authors[0]
              title = authors[1]
              sold = int(authors[2])
              if sold >= 4000:
                            due = sold * 0.35
              else:
                            due = sold * 0.29
              #endif
              # accumulate and count
              ta = ta + 1
              tb = tb + sold
              tr = tr + due
              #output
              #print(name,title,sold,due)
              print( "%10s      %10s       %12i    %12.2f"   %  (name,title,sold,due))
#end for
bookfile.close()

print("  Total authors found   ==> ",ta)
print("  Total books           ==> ",tb)
print("  Total royalities      ==> $", round(tr,2))
print("\n .... End of job!")
bookfile.close()
# end of main
