with open('templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Overhaul #products section
prods_start = text.find('id="products"')
prods_end = text.find('</section>', prods_start)

old_prods_block = text[prods_start:prods_end+10]

# Replace text-white in products titles and prices
new_prods_block = old_prods_block.replace(
    'text-2xl sm:text-4xl font-black text-white mt-1',
    'text-2xl sm:text-4xl font-black text-stone-900 mt-1'
)
new_prods_block = new_prods_block.replace(
    'class="luxury-card rounded-2xl p-4 flex flex-col justify-between border border-slate-800 hover:border-gold-500/30 transition group"',
    'class="bg-white rounded-2xl p-4 flex flex-col justify-between border border-stone-200 shadow-sm hover:border-amber-400 hover:shadow-md transition group"'
)
new_prods_block = new_prods_block.replace(
    'class="font-bold text-xs sm:text-sm text-white group-hover:text-gold-300 transition line-clamp-1"',
    'class="font-black text-sm text-stone-900 group-hover:text-amber-600 transition line-clamp-1"'
)
new_prods_block = new_prods_block.replace(
    'class="text-[11px] text-slate-400 mt-1 line-clamp-2"',
    'class="text-xs text-stone-500 mt-1 line-clamp-2 leading-relaxed"'
)
new_prods_block = new_prods_block.replace(
    'class="text-base font-black text-white"',
    'class="text-lg font-black text-stone-900"'
)
new_prods_block = new_prods_block.replace(
    'class="text-[10px] text-slate-400 ml-0.5"',
    'class="text-xs text-stone-500 font-bold ml-1"'
)
new_prods_block = new_prods_block.replace(
    'class="w-full bg-dark-800 hover:bg-gold-500 hover:text-dark-900 text-slate-200 font-bold py-2 rounded-xl text-xs border border-slate-700 hover:border-gold-400 transition flex items-center justify-center space-x-1"',
    'class="w-full bg-amber-500 hover:bg-amber-600 text-stone-950 font-black py-2.5 rounded-xl text-xs transition shadow flex items-center justify-center space-x-1.5 cursor-pointer"'
)

text = text[:prods_start] + new_prods_block + text[prods_end+10:]

# 2. Overhaul #custom-builder section
builder_start = text.find('id="custom-builder"')
builder_end = text.find('</section>', builder_start)
old_builder_block = text[builder_start:builder_end+10]

new_builder_block = old_builder_block.replace(
    'class="font-bold text-xs text-white line-clamp-1"',
    'class="font-black text-xs text-stone-900 line-clamp-1 mb-1"'
)
new_builder_block = new_builder_block.replace(
    'class="text-[10px] text-slate-400 mt-0.5"',
    'class="text-[11px] text-stone-500 font-bold mt-0.5"'
)
new_builder_block = new_builder_block.replace(
    'class="luxury-card p-3 rounded-2xl border border-slate-700/80 flex flex-col justify-between text-center hover:border-gold-500/40 transition"',
    'class="bg-white p-3 rounded-2xl border border-stone-200 shadow-sm flex flex-col justify-between text-center hover:border-amber-400 transition"'
)
new_builder_block = new_builder_block.replace(
    'class="w-6 h-6 rounded-lg bg-dark-900 border border-slate-700 text-slate-300 hover:text-white text-xs"',
    'class="w-7 h-7 rounded-lg bg-stone-100 hover:bg-stone-200 border border-stone-300 text-stone-800 font-black text-xs cursor-pointer"'
)
new_builder_block = new_builder_block.replace(
    'class="w-6 h-6 rounded-lg bg-gradient-to-r from-gold-500 to-amber-600 text-dark-900 font-bold text-xs"',
    'class="w-7 h-7 rounded-lg bg-amber-500 hover:bg-amber-600 text-stone-950 font-black text-xs cursor-pointer"'
)
new_builder_block = new_builder_block.replace(
    'class="font-bold text-xs text-white w-4"',
    'class="font-black text-sm text-stone-900 w-5"'
)

text = text[:builder_start] + new_builder_block + text[builder_end+10:]

# 3. Overhaul #promo section
promo_start = text.find('id="promo"')
promo_end = text.find('</section>', promo_start)
old_promo_block = text[promo_start:promo_end+10]

new_promo_block = old_promo_block.replace(
    'text-2xl sm:text-4xl font-black text-white mt-1',
    'text-2xl sm:text-4xl font-black text-stone-900 mt-1'
)
new_promo_block = new_promo_block.replace(
    'class="luxury-card rounded-3xl p-6 border',
    'class="bg-white rounded-3xl p-6 border border-stone-200 shadow-sm'
)
new_promo_block = new_promo_block.replace(
    'class="text-xl font-black text-white group-hover:text-gold-300',
    'class="text-xl font-black text-stone-900 group-hover:text-amber-600'
)
new_promo_block = new_promo_block.replace(
    'class="text-2xl font-black text-white"',
    'class="text-2xl font-black text-stone-900"'
)

text = text[:promo_start] + new_promo_block + text[promo_end+10:]

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('All sections successfully overhauled with crystal clear high-contrast typography!')
