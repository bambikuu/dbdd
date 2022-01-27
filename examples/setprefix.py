@client.command()
async def setprefix(ctx, prefixset):
    prefix = prefixset
    await ctx.send(f"Prefix changed to ``{prefixset}``")