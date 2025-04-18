import nextcord
from nextcord.ext import commands
from nextcord.ui import View, Button

role_id = 1350768567242588170

class RoleView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="รับยศ", style=nextcord.ButtonStyle.gray, emoji="🔘")
    async def get_role(self, button: Button, interaction: nextcord.Interaction):
        role = interaction.guild.get_role(role_id)
        if role is None:
            await interaction.response.send_message("ไม่พบยศ! ตรวจสอบ role_id ด้วยนะ!", ephemeral=True)
            return

        if role in interaction.user.roles:
            await interaction.response.send_message("⚠️ คุณมียศนี้อยู่แล้ว", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"✅ เพิ่มยศ `{role.name}` ให้เรียบร้อยแล้ว", ephemeral=True)

    @nextcord.ui.button(label="เช็คยศ", style=nextcord.ButtonStyle.gray, emoji="⚙")
    async def check_role(self, button: Button, interaction: nextcord.Interaction):
        roles = [role.name for role in interaction.user.roles if role.id != interaction.guild.id]
        role_list = ", ".join(roles) if roles else "ไม่มียศเลยน้า~"
        await interaction.response.send_message(f"🔍 ยศของคุณ: {role_list}", ephemeral=True)

    @nextcord.ui.button(label="รายละเอียดดิส", style=nextcord.ButtonStyle.gray, emoji="⏰")
    async def check_members(self, button: Button, interaction: nextcord.Interaction):
        guild = interaction.guild
        member_count = guild.member_count
        await interaction.response.send_message(f"🌐 เซิร์ฟเวอร์ `{guild.name}` มีสมาชิกทั้งหมด: {member_count} คน", ephemeral=True)

class RoleMember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def get_role(self, ctx):
        guild = ctx.guild
        icon_url = guild.icon.url if guild.icon else None
        embed = nextcord.Embed(
            title="__ระบบรับยศ Verify__",
            description=(
                "`🟢` **รับยศเพื่อ ดูเซิร์ฟ**\n"
                "- กดปุ่มด้านล่างเพื่อรับยศ\n"
                "- ผู้สร้าง: **Mr Emptiness**\n"
                "- ```discord.gg/x3XkCBswvY```"
            ),
            color=0x780cc5
        )
        if icon_url:
            embed.set_thumbnail(url=icon_url)
        embed.set_image(url="https://i.pinimg.com/originals/d6/6a/d1/d66ad1a0ce0fc09370424075125b06b7.gif")
        embed.set_footer(text=f"รับยศด้วยนะ~")
        await ctx.send(embed=embed, view=RoleView())

def setup(bot):
    bot.add_cog(RoleMember(bot))
