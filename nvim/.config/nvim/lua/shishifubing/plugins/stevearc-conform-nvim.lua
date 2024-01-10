return {
    {
        "stevearc/conform.nvim",
        dependencies = {
            "neovim/nvim-lspconfig",
            "nvim-lua/plenary.nvim",
            "williamboman/mason.nvim",
        },
        event = { "BufWritePre" },
        cmd = { "ConformInfo" },
        opts = {
            formatters_by_ft = {
                lua = { "stylua" },
                python = { "isort", "black" },
                bash = { "shfmt", "shellcheck" },
                sh = { "shfmt", "shellcheck" },
                go = { "goimports", "gofumpt", "goimports-reviser" },
                javascript = { { "prettierd", "prettier" } },
                typescript = { { "prettierd", "prettier" } },
                vue = { { "prettierd", "prettier" } },
                css = { { "prettierd", "prettier" } },
                scss = { { "prettierd", "prettier" } },
                less = { { "prettierd", "prettier" } },
                html = { { "prettierd", "prettier" } },
                json = { { "prettierd", "prettier" } },
                jsonc = { { "prettierd", "prettier" } },
                markdown = { { "prettierd", "prettier" } },
                yaml = { { "prettierd", "prettier" } },
            },
            format_on_save = {
                timeout_ms = 2000,
                lsp_fallback = true,
            },
            formatters = {
                shfmt = {
                    prepend_args = { "-i", "4" },
                },
            },
        },
    },
}
