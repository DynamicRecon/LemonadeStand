#LEMONADE STAND

##DESCRIPTION
    This my attempt to re-create the basic lemonade stand game using django and simpy to
simulate weather, supplier/inventory, and sales. 


##Objective
    Keep the stand open for as long as possible. Weather Effects and your price
    can affect the outcome at Day close. You keep the lemonade stand open for 
    8 hours.

##How to play
    1. Open Home Page.
        *Start Date: 6/4/1955 7:00:00 AM
    2. You start out with $2.00. (Starting assets)
        *With a cost of lemons of $0.10 per cup. 
        *A cost of Sugar of $0.05 per cup. 
        *A cost cost of signs at $0.15 per sign. 
    
    3. You enter number of cups of lemonade to make then number of signs to make.
            *Finally you decide on a price.
    
    4. You click: "Open"
         *Live data is displayed and Hours are counted up in Game Time.
    
    5. @04:00:00 PM Stand Closes. 
        *All unsold lemonade is thrown out signs ripped up. 
        *Profits = totals_costs - sales.
    
    6. New Day begins. Return to home page.
        *Weather report will be displayed.
        *Sales report will be displayed.

    *Note: If your assets drops below zero you are closed for business.*


