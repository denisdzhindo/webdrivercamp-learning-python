XPath

Resources

HTML Document Tree http://web.simmons.edu/~grabiner/comm244/weekfour/document-tree.html

XPath - Tutorial https://www.w3schools.com/xml/xpath_intro.asp 

Core XPath Functions https://developer.mozilla.org/en-US/docs/Web/XPath/Functions


0. Find Headers
Write an XPath that collects all the header links ( located under the search field ) here [ebay](https://www.ebay.com/) 

1. Find filter sections
Write an XPath that collects left navigation blocks here [ebay / shoes](https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=shoes&_sacat=0)
US Shoe Size
Brand
Color
Upper Material
Occasion
Department
Condition
Price
Buying Format
Item Location
Shipping Options
Local Pickup
Show Only

2. Now make it dynamic
Modify the XPath from task #1 to make it dynamic:
So we can select a specific section based on the header of the section
//some_xpath..."Brand" - would point to Brand section
//same_xpath..."Color" - would point to Brand section

3. Add the checkboxes
Modify the XPath from task #2 to select specific checkboxes of the specific section
//some_xpath..."Brand"..."adidas" - would point to Brand section to checkbox named adidas
//same_xpath..."Color"..."Blue" - would point to Color section to checkbox named blue

4. Make it case insensitive
Write an XPath to collect all items here [ebay / shoes](https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=shoes&_sacat=0)
Add an option to select an item by title
This XPath should work with passing a title in lower case only

5. Pause it
Write an XPath to collect the links in the dropdown My eBay here [ebay / shoes](https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=shoes&_sacat=0)
To see the links pause the page when dropdown is open
When you work with the XPath - the dropdown should not close
As the answer to this question - write how you pause the page next to XPath

Advanced

Give me what I want
Go here [ebay / watches ](https://www.ebay.com/sch/i.html?_from=R40&_nkw=watch&_sacat=0&rt=nc&Department=Men&_dcat=31387)
Find an XPath to collect watches that are:

$20 < price < $200

5.0 out of 5 stars and reviews count >= 10

Free shipping

Are on Sale: 20% 0ff and more

Note: It should be one single XPath to complete the task


Summary

Basics of HTML and Document Tree.

What is XPath?

XPath’s Operators, Functions, Axes

The differences between relative and absolute XPaths?

Ways to write Dynamic XPaths

Is XPath a query language?

Is relative XPath expression better than absolute XPath expression?
