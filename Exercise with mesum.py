can_per_pack= 6
pack_price = float( input( "What is price of 6 pack= "))
can_volume = float( input ("What is volume of each can(in ml)= "))
pack_volume_in_ml = (can_per_pack * can_volume)
print(pack_volume_in_ml)
price_per_ml =   pack_price/ pack_volume_in_ml
print(price_per_ml)
price_per_pack = price_per_ml*can_volume
print(price_per_ml)
price_per_pack = pack_price/can_per_pack
print(price_per_pack)
price_per_liter= price_per_ml *1000
print(price_per_liter)