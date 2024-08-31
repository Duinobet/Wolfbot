div_base = 1e8
hedge    = 99
bethigh  = true
low_rate = true
chance_bet = 10
ls_limit   = 1e2 / chance_bet
chance     = chance_bet
payout     = (hedge / chance) - 1
max_balance = 10
basebet     = max_balance / div_base
bazebet     = (max_balance / (div_base/100)) / ls_limit
multi       = bazebet
nextbet     = basebet
betz = 0
winz = 0
ws   = 0
ls   = 0
current_profit = 0
partial_profit = 0
previous_bethigh = bethigh
previous_chance  = chance
previous_payout  = payout
previous_bet     = nextbet
function dobet()
    betz         = betz + 1
    trigger_stop = betz / ls_limit
    if (win) then
        ls             = 0
        ws             = ws + 1
        winz           = winz + 1
        bethigh        = not bethigh
        rate_wins      = 1e2 - (trigger_stop / winz * 1e2)
        current_profit = previous_bet * previous_payout
    else
        ws = 0
        ls = ls + 1
        current_profit = -previous_bet
    end
    partial_profit = partial_profit + current_profit
    if (partial_profit >= 0) then
        resetpartialprofit()
        partial_profit = 0
        max_balance    = 10
    end
    if (ws > 0) then
        if (rate_wins < 50) then
            betz       = 0
            winz       = 0
            chance_bet = math.random(10)
            if (chance_bet == previous_chance) then
                chance_bet = chance_bet + 1
            end
            ls_limit = 1e2 / chance_bet
            basebet  = max_balance / div_base
            low_rate = true
            chance   = chance_bet
            payout   = (hedge / chance) - 1
            nextbet  = basebet
        else
            low_rate = false
            bazebet  = (max_balance / (div_base/100)) / ls_limit
            multi    = bazebet
            nextbet  = multi
        end
    end
    if (ls > 0) then
        trigger_multi = math.floor(ls_limit * 5)
        if (ls > trigger_multi) then
            nextbet = (-partial_profit) / payout
        elseif (low_rate) then
            nextbet = (-partial_profit) / payout + basebet
        else
            multi   = multi + bazebet
            nextbet = (-partial_profit) / payout + multi
        end
    end
    previous_bethigh = bethigh
    previous_chance  = chance
    previous_payout  = payout
    previous_bet     = nextbet
end
