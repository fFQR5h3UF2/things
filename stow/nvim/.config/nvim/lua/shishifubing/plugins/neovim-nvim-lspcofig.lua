return {
    {
        -- LSP Configuration & Plugins
        "neovim/nvim-lspconfig",
        dependencies = {
            -- Automatically install LSPs to stdpath for neovim
            "williamboman/mason.nvim",
            "williamboman/mason-lspconfig.nvim",
            -- Useful status updates for LSP
            { "j-hui/fidget.nvim", version = "*", opts = {} },
            -- Additional lua configuration, makes nvim stuff amazing!
            "folke/neodev.nvim",
        },
        config = function()
            local servers = {
                ansiblels = {},
                gopls = {},
                bashls = {},
                clangd = {},
                pyright = {},
                dockerls = {},
                docker_compose_language_service = {},
                gradle_ls = {},
                helm_ls = {},
                kotlin_language_server = {},
                marksman = {},
                taplo = {},
                jsonls = {},
                tflint = {},
                html = {},
                yamlls = {
                    settings = {
                        yaml = {
                            completion = true,
                            hover = true,
                            validate = true,
                            schemaStore = {
                                enable = true,
                            },
                            customTags = {
                                "!reference sequence",
                            },
                        },
                    },
                },
                lua_ls = {
                    Lua = {
                        workspace = { checkThirdParty = false },
                        telemetry = { enable = false },
                        diagnostics = {
                            globals = { "vim" },
                            disable = { "missing-fields" },
                        },
                    },
                },
            }

            local cmp_nvim_lsp = require("cmp_nvim_lsp")
            local mason = require("mason")
            local mason_lspconfig = require("mason-lspconfig")
            local lspconfig = require("lspconfig")
            local neodev = require("neodev")
            local keymaps = require("shishifubing.keymaps")
            local on_attach = keymaps.set_lsp

            local capabilities = cmp_nvim_lsp.default_capabilities(
                vim.lsp.protocol.make_client_capabilities()
            )

            neodev.setup()
            mason.setup()
            mason_lspconfig.setup({
                ensure_installed = vim.tbl_keys(servers),
            })
            mason_lspconfig.setup_handlers({
                function(server_name)
                    lspconfig[server_name].setup({
                        capabilities = capabilities,
                        on_attach = on_attach,
                        settings = servers[server_name],
                        filetypes = (servers[server_name] or {}).filetypes,
                    })
                end,
            })
        end,
    },
}
