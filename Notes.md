# Compound interest
## basic interest

If you put money$ as your money into the bank and your interest is percent%, then you will get percent*money per year

<code>
    
    money = 48_000
    percent = 0.5

    for years in (1,10):
        money += money*percent*years
        
</code>
<hr>

## compound interest

formula:

<code>

    starting_money = 70_000
    percent = 0.9999
    ending_money = 0

    for years in range(1,10)
        ending_money += starting_money*(1+percent)

</code>
