return {
    -- Autocompletion
    "hrsh7th/nvim-cmp",
    dependencies = {
        -- Snippet Engine & its associated nvim-cmp source
        { "L3MON4D3/LuaSnip" },
        { "saadparwaiz1/cmp_luasnip" },

        -- Adds LSP completion capabilities
        { "hrsh7th/cmp-nvim-lsp" },
        { "hrsh7th/cmp-path" },

        -- Adds a number of user-friendly snippets
        { "rafamadriz/friendly-snippets" },
    },
    config = function()
        local cmp = require("cmp")
        local luasnip = require("luasnip")

        require("luasnip.loaders.from_vscode").lazy_load()
        require("luasnip.loaders.from_snipmate").lazy_load()
        luasnip.config.setup({})

        cmp.setup({
            snippet = {
                expand = function(args)
                    luasnip.lsp_expand(args.body)
                end,
            },
            mapping = require("shishifubing.keymaps").get_cmp(),
            sources = {
                { name = "nvim_lsp" },
                { name = "luasnip" },
                { name = "path" },
            },
        })
    end,
}
