resetseed() 
chance  = 30 
base    = 1e-5
nextbet = base 
roll    = 0 
inc     = 1.2 
opit    = 0 
x       = 0 
function dobet() 
roll = roll+1 
if win and balance > x then 
x = balance 
nextbet = base 
chance = 30 
resetpartialprofit() 
end 
 
if (chance == 30) then 
if win then 
  nextbet = base 
  chance = 30 
else 
  nextbet = previousbet*1.08 
end 
end 
if currentstreak<(-3)*2 then 
  nextbet = previousbet 
  chance = 19.8 
if win then 
     nextbet = base 
     chance = 30 
  else 
     nextbet = previousbet*1.2 
  end 
end 
if currentstreak<(-5)*3 then 
  nextbet = previousbet 
  chance = 10 
  if win then 
     nextbet = base 
     chance = 30 
  else 
     nextbet = previousbet*1.12 
  end 
end 
end
