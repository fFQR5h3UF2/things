return {
    {
        -- LSP Configuration & Plugins
        "neovim/nvim-lspconfig",
        dependencies = {
            -- Automatically install LSPs to stdpath for neovim
            "williamboman/mason.nvim",
            "williamboman/mason-lspconfig.nvim",
            -- Useful status updates for LSP
            "j-hui/fidget.nvim",
            -- Additional lua configuration, makes nvim stuff amazing!
            "folke/neodev.nvim",
        },
        config = function()
            local servers = {
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
                html = { filetypes = { "html", "twig", "hbs" } },
                yamlls = {
                    settings = {
                        yaml = {
                            format = {
                                enable = true,
                                printWidth = 80,
                            },
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
            local fidget = require("fidget")
            local neodev = require("neodev")
            local on_attach =
                require("shishifubing.keymaps").on_buffer_attach_lsp

            local capabilities = cmp_nvim_lsp.default_capabilities(
                vim.lsp.protocol.make_client_capabilities()
            )

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
            fidget.setup()
            neodev.setup()

            -- Create an augroup that is used for managing our formatting autocmds.
            --      We need one augroup per client to make sure that multiple clients
            --      can attach to the same buffer without interfering with each other.
            local _augroups = {}
            local get_augroup = function(client)
                if not _augroups[client.id] then
                    local group_name = "kickstart-lsp-format-" .. client.name
                    local id = vim.api.nvim_create_augroup(
                        group_name,
                        { clear = true }
                    )
                    _augroups[client.id] = id
                end

                return _augroups[client.id]
            end

            -- Whenever an LSP attaches to a buffer, we will run this function.
            --
            -- See `:help LspAttach` for more information about this autocmd event.
            vim.api.nvim_create_autocmd("LspAttach", {
                group = vim.api.nvim_create_augroup(
                    "kickstart-lsp-attach-format",
                    { clear = true }
                ),
                -- This is where we attach the autoformatting for reasonable clients
                callback = function(args)
                    local client_id = args.data.client_id
                    local client = vim.lsp.get_client_by_id(client_id)
                    local bufnr = args.buf

                    -- Only attach to clients that support document formatting
                    if
                        not client.server_capabilities.documentFormattingProvider
                    then
                        return
                    end

                    -- Tsserver usually works poorly. Sorry you work with bad languages
                    -- You can remove this line if you know what you're doing :)
                    if client.name == "tsserver" then
                        return
                    end

                    -- Create an autocmd that will run *before* we save the buffer.
                    --  Run the formatting command for the LSP that has just attached.
                    vim.api.nvim_create_autocmd("BufWritePre", {
                        group = get_augroup(client),
                        buffer = bufnr,
                        callback = function()
                            vim.lsp.buf.format({
                                async = false,
                                filter = function(c)
                                    return c.id == client.id
                                end,
                            })
                        end,
                    })
                end,
            })
        end,
    },
}
