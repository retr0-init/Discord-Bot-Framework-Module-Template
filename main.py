'''
Discord-Bot-Module template. For detailed usages,
 check https://interactions-py.github.io/interactions.py/
'''
import interactions
# Use the following method to import the internal module in the current same directory
from . import internal_t

'''
Replace the ModuleName with any name you'd like
'''
class ModuleName(interactions.Extension):
    module_base: interactions.SlashCommand = interactions.SlashCommand(
        name="replace_your_command_base_here",
        description="Replace here for the base command descriptions"
    )
    module_group: interactions.SlashCommand = self.module_base.group(
        name="replace_your_command_group_here",
        description="Replace here for the group command descriptions"
    )

    @self.module_group.subcommand("ping", sub_cmd_description="Replace the description of this command")
    @interactions.slash_option(
        name = "option_name",
        description = "Option description",
        required = True,
        opt_type = interactions.OptionType.STRING
    )
    async def module_group_ping(self, ctx: interactions.SlashContext, option_name: str):
        await ctx.send(f"Pong {option_name}!")
        internal_t.internal_t_testfunc()

    @self.module_base.subcommand("pong", sub_cmd_description="Replace the description of this command")
    @interactions.slash_option(
        name = "option_name",
        description = "Option description",
        required = True,
        opt_type = interactions.OptionType.STRING
    )
    async def module_group_pong(self, ctx: interactions.SlashContext, option_name: str):
        await ctx.send(f"Pong {option_name}!")
        internal_t.internal_t_testfunc()