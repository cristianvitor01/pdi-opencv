
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define N 5  // Ordem da árvore B+

typedef struct {
    char codigo_barra[13];
    char nome[100];
    char data_cadastro[11];
    int quantidade;
    float preco;
} Medicamento;

typedef struct page {
    int qnt;
    bool folha;
    char codigos[N - 1][13];
    struct page* pai;
    Medicamento* medicamentos[N - 1];
    struct page* filhos[N];
    struct page* prox;
} Pagina;

// Função para criar uma nova página
Pagina* criar_pagina(bool folha) {
    Pagina* nova_pagina = (Pagina*)malloc(sizeof(Pagina));
    nova_pagina->qnt = 0;
    nova_pagina->folha = folha;
    nova_pagina->pai = NULL;
    nova_pagina->prox = NULL;
    for (int i = 0; i < N; i++) {
        nova_pagina->filhos[i] = NULL;
    }
    return nova_pagina;
}

// Função para criar um novo medicamento
Medicamento* criar_medicamento(const char* codigo_barra, const char* nome, const char* data_cadastro, int quantidade, float preco) {
    Medicamento* novo = (Medicamento*)malloc(sizeof(Medicamento));
    strcpy(novo->codigo_barra, codigo_barra);
    strcpy(novo->nome, nome);
    strcpy(novo->data_cadastro, data_cadastro);
    novo->quantidade = quantidade;
    novo->preco = preco;
    return novo;
}

// Função para atualizar a quantidade de um medicamento existente
void atualizar_quantidade(Pagina* pagina, int indice, int quantidade_adicional) {
    pagina->medicamentos[indice]->quantidade += quantidade_adicional;
}

// Função para encontrar a posição correta de inserção
int encontrar_posicao(Pagina* pagina, const char* codigo_barra) {
    int i = 0;
    while (i < pagina->qnt && strcmp(pagina->codigos[i], codigo_barra) < 0) {
        i++;
    }
    return i;
}

// Função para inserir um novo medicamento em uma página não cheia
void inserir_em_pagina(Pagina* pagina, Medicamento* medicamento, int pos) {
    for (int i = pagina->qnt; i > pos; i--) {
        strcpy(pagina->codigos[i], pagina->codigos[i - 1]);
        pagina->medicamentos[i] = pagina->medicamentos[i - 1];
    }
    strcpy(pagina->codigos[pos], medicamento->codigo_barra);
    pagina->medicamentos[pos] = medicamento;
    pagina->qnt++;
}

// Função para dividir uma página
void dividir_pagina(Pagina* pagina, Pagina** raiz, int pos) {
    Pagina* nova_pagina = criar_pagina(pagina->folha);
    int meio = (N - 1) / 2;
    int i, j;

    // Copiar dados para a nova página
    nova_pagina->qnt = pagina->qnt - meio - 1;
    for (i = meio + 1, j = 0; i < pagina->qnt; i++, j++) {
        strcpy(nova_pagina->codigos[j], pagina->codigos[i]);
        nova_pagina->medicamentos[j] = pagina->medicamentos[i];
    }
    if (!pagina->folha) {
        for (i = meio + 1, j = 0; i <= pagina->qnt; i++, j++) {
            nova_pagina->filhos[j] = pagina->filhos[i];
            if (nova_pagina->filhos[j] != NULL) {
                nova_pagina->filhos[j]->pai = nova_pagina;
            }
        }
    }
    pagina->qnt = meio;

    // Inserir o meio no pai
    if (pagina->pai == NULL) {
        Pagina* nova_raiz = criar_pagina(false);
        strcpy(nova_raiz->codigos[0], pagina->codigos[meio]); // Usando strcpy aqui
        nova_raiz->filhos[0] = pagina;
        nova_raiz->filhos[1] = nova_pagina;
        nova_raiz->qnt = 1;
        pagina->pai = nova_raiz;
        nova_pagina->pai = nova_raiz;
        *raiz = nova_raiz;
    } else {
        Pagina* pai = pagina->pai;
        int pos_pai = encontrar_posicao(pai, pagina->codigos[meio]);
        for (i = pai->qnt; i > pos_pai; i--) {
            strcpy(pai->codigos[i], pai->codigos[i - 1]); // Usando strcpy aqui
            pai->filhos[i + 1] = pai->filhos[i];
        }
        strcpy(pai->codigos[pos_pai], pagina->codigos[meio]); // Usando strcpy aqui
        pai->filhos[pos_pai + 1] = nova_pagina;
        pai->qnt++;
        nova_pagina->pai = pai;
    }
}

// Função para inserir um medicamento na árvore B+
void inserir_medicamento(Pagina** raiz, Medicamento* medicamento) {
    Pagina* pagina_atual = *raiz;
    Pagina* pai = NULL;
    Pagina* nova_pagina = NULL;
    int pos;

    while (!pagina_atual->folha) {
        pos = encontrar_posicao(pagina_atual, medicamento->codigo_barra);
        pai = pagina_atual;
        pagina_atual = pagina_atual->filhos[pos];
    }

    pos = encontrar_posicao(pagina_atual, medicamento->codigo_barra);
    if (pos < pagina_atual->qnt && strcmp(pagina_atual->codigos[pos], medicamento->codigo_barra) == 0) {
        // Atualizar quantidade se o medicamento já existe
        atualizar_quantidade(pagina_atual, pos, medicamento->quantidade);
        free(medicamento);
    } else {
        // Inserir novo medicamento
        if (pagina_atual->qnt < N - 1) {
            inserir_em_pagina(pagina_atual, medicamento, pos);
        } else {
            dividir_pagina(pagina_atual, raiz, pos);
            // A divisão pode mudar a raiz
            if (*raiz != pagina_atual->pai) {
                inserir_medicamento(raiz, medicamento);
            }
        }
    }
}

// Função para buscar um medicamento pelo código de barras
Medicamento* buscar_medicamento(Pagina* raiz, const char* codigo_barra) {
    Pagina* atual = raiz;
    while (atual != NULL) {
        if (atual->folha) {
            for (int i = 0; i < atual->qnt; i++) {
                if (strcmp(atual->codigos[i], codigo_barra) == 0) {
                    return atual->medicamentos[i];
                }
            }
            return NULL;
        } else {
            int i = 0;
            while (i < atual->qnt && strcmp(codigo_barra, atual->codigos[i]) > 0) {
                i++;
            }
            atual = atual->filhos[i];
        }
    }
    return NULL;
}

// Função para redistribuir ou fundir páginas
void redistribuir_ou_fundir(Pagina* pagina, int pos) {
    Pagina* pai = pagina->pai;
    Pagina* pagina_irmao;
    int meio;

    if (pagina->qnt >= (N - 1) / 2) {
        return;
    }

    if (pos > 0) {
        // Página não é a primeira filha
        pagina_irmao = pai->filhos[pos - 1];
        if (pagina_irmao->qnt > (N - 1) / 2) {
            // Redistribuição
            meio = pagina_irmao->qnt - 1;
            for (int i = pagina->qnt; i > 0; i--) {
                strcpy(pagina->codigos[i], pagina->codigos[i - 1]);
                pagina->medicamentos[i] = pagina->medicamentos[i - 1];
            }
            strcpy(pagina->codigos[0], pai->codigos[pos - 1]);
            pagina->medicamentos[0] = pagina_irmao->medicamentos[meio];
            strcpy(pai->codigos[pos - 1], pagina_irmao->codigos[meio]);
            pagina->qnt++;
            pagina_irmao->qnt--;
            return;
        }
    } else {
        // Página é a primeira filha
        pagina_irmao = pai->filhos[1];
        if (pagina_irmao->qnt > (N - 1) / 2) {
            // Redistribuição
            meio = 0;
            for (int i = pagina->qnt; i > 0; i--) {
                strcpy(pagina->codigos[i], pagina->codigos[i - 1]);
                pagina->medicamentos[i] = pagina->medicamentos[i - 1];
            }
            strcpy(pagina->codigos[0], pai->codigos[0]);
            pagina->medicamentos[0] = pagina_irmao->medicamentos[0];
            strcpy(pai->codigos[0], pagina_irmao->codigos[0]);
            pagina->qnt++;
            pagina_irmao->qnt--;
            return;
        }
    }

    // Fusão
    if (pagina_irmao->qnt < (N - 1) / 2) {
        // Mover todos os elementos para a página pai e fundir
        if (pos > 0) {
            int qnt_original_irmao = pagina_irmao->qnt;
            pagina_irmao->qnt += pagina->qnt + 1;
            for (int i = 0; i < pagina->qnt; i++) {
                strcpy(pagina_irmao->codigos[qnt_original_irmao + i], pagina->codigos[i]);
                pagina_irmao->medicamentos[qnt_original_irmao + i] = pagina->medicamentos[i];
            }
            for (int i = pos; i < pai->qnt - 1; i++) {
                strcpy(pai->codigos[i], pai->codigos[i + 1]);
                pai->filhos[i + 1] = pai->filhos[i + 2];
            }
            pai->qnt--;
        } else {
            int qnt_original_pagina = pagina->qnt;
            pagina->qnt += pagina_irmao->qnt + 1;
            for (int i = 0; i < pagina_irmao->qnt; i++) {
                strcpy(pagina->codigos[qnt_original_pagina + i], pagina_irmao->codigos[i]);
                pagina->medicamentos[qnt_original_pagina + i] = pagina_irmao->medicamentos[i];
            }
            for (int i = pos + 1; i < pai->qnt; i++) {
                strcpy(pai->codigos[i - 1], pai->codigos[i]);
                pai->filhos[i] = pai->filhos[i + 1];
            }
            pai->qnt--;
        }
        free(pagina_irmao);
    }
}


// Função para remover um medicamento de uma página
void remover_medicamento_de_pagina(Pagina* pagina, int pos) {
    for (int i = pos; i < pagina->qnt - 1; i++) {
        strcpy(pagina->codigos[i], pagina->codigos[i + 1]);
        pagina->medicamentos[i] = pagina->medicamentos[i + 1];
    }
    pagina->qnt--;
}

// Função para buscar e remover um medicamento
void remover_medicamento(Pagina** raiz, const char* codigo_barra, int quantidade) {
    Pagina* pagina_atual = *raiz;
    int pos;

    while (!pagina_atual->folha) {
        pos = encontrar_posicao(pagina_atual, codigo_barra);
        pagina_atual = pagina_atual->filhos[pos];
    }

    pos = encontrar_posicao(pagina_atual, codigo_barra);
    if (pos < pagina_atual->qnt && strcmp(pagina_atual->codigos[pos], codigo_barra) == 0) {
        if (pagina_atual->medicamentos[pos]->quantidade > quantidade) {
            pagina_atual->medicamentos[pos]->quantidade -= quantidade;
        } else {
            free(pagina_atual->medicamentos[pos]);
            remover_medicamento_de_pagina(pagina_atual, pos);
            while (pagina_atual->pai != NULL && pagina_atual->qnt < (N - 1) / 2) {
                pos = encontrar_posicao(pagina_atual->pai, pagina_atual->codigos[0]);
                redistribuir_ou_fundir(pagina_atual, pos);
                pagina_atual = pagina_atual->pai;
            }
            if (pagina_atual->qnt == 0 && pagina_atual->pai == NULL) {
                free(pagina_atual);
                *raiz = NULL;
            }
        }
    } else {
        printf("Medicamento não encontrado.\n");
    }
}

// Função para imprimir todos os medicamentos em ordem
void imprimir_todos_medicamentos(Pagina* raiz) {
    if (raiz == NULL) {
        return;
    }

    // Encontrar a folha mais à esquerda
    Pagina* folha_atual = raiz;
    while (!folha_atual->folha) {
        folha_atual = folha_atual->filhos[0];
    }

    // Percorrer as folhas e imprimir medicamentos
    while (folha_atual != NULL) {
        for (int i = 0; i < folha_atual->qnt; i++) {
            Medicamento* med = folha_atual->medicamentos[i];
            printf("Código de Barras: %s\n", med->codigo_barra);
            printf("Nome: %s\n", med->nome);
            printf("Data de Cadastro: %s\n", med->data_cadastro);
            printf("Quantidade: %d\n", med->quantidade);
            printf("Preço: %.2f\n\n", med->preco);
        }
        folha_atual = folha_atual->prox;
    }
}

int main() {
    Pagina* raiz = criar_pagina(true);
    int opcao;
    char codigo_barra[13];
    char nome[100];
    char data_cadastro[11];
    int quantidade;
    float preco;
    Medicamento* medicamento;

    do {
        printf("Menu:\n");
        printf("1. Inserir medicamento\n");
        printf("2. Remover medicamento\n");
        printf("3. Buscar medicamento\n");
        printf("4. Imprimir todos os medicamentos\n");
        printf("5. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);
        getchar();  // Limpar o buffer do newline

        switch (opcao) {
            case 1:  // Inserir medicamento
                printf("Digite o código de barras: ");
                fgets(codigo_barra, sizeof(codigo_barra), stdin);
                codigo_barra[strcspn(codigo_barra, "\n")] = '\0';  // Remover newline

                printf("Digite o nome: ");
                fgets(nome, sizeof(nome), stdin);
                nome[strcspn(nome, "\n")] = '\0';  // Remover newline

                printf("Digite a data de cadastro (dd/mm/aaaa): ");
                fgets(data_cadastro, sizeof(data_cadastro), stdin);
                data_cadastro[strcspn(data_cadastro, "\n")] = '\0';  // Remover newline

                printf("Digite a quantidade: ");
                scanf("%d", &quantidade);

                printf("Digite o preço: ");
                scanf("%f", &preco);
                getchar();  // Limpar o buffer do newline

                medicamento = criar_medicamento(codigo_barra, nome, data_cadastro, quantidade, preco);
                inserir_medicamento(&raiz, medicamento);
                printf("Medicamento inserido com sucesso.\n");
                break;

            case 2:  // Remover medicamento
                printf("Digite o código de barras do medicamento a ser removido: ");
                fgets(codigo_barra, sizeof(codigo_barra), stdin);
                codigo_barra[strcspn(codigo_barra, "\n")] = '\0';  // Remover newline

                printf("Digite a quantidade a ser removida: ");
                scanf("%d", &quantidade);
                getchar();  // Limpar o buffer do newline

                remover_medicamento(&raiz, codigo_barra, quantidade);
                printf("Medicamento removido com sucesso (se existia).\n");
                break;

            case 3:  // Buscar medicamento
                printf("Digite o código de barras do medicamento a ser buscado: ");
                fgets(codigo_barra, sizeof(codigo_barra), stdin);
                codigo_barra[strcspn(codigo_barra, "\n")] = '\0';  // Remover newline

                medicamento = buscar_medicamento(raiz, codigo_barra);
                if (medicamento) {
                    printf("Código de Barras: %s\n", medicamento->codigo_barra);
                    printf("Nome: %s\n", medicamento->nome);
                    printf("Data de Cadastro: %s\n", medicamento->data_cadastro);
                    printf("Quantidade: %d\n", medicamento->quantidade);
                    printf("Preço: %.2f\n", medicamento->preco);
                } else {
                    printf("Medicamento não encontrado.\n");
                }
                break;

            case 4:  // Imprimir todos os medicamentos
                imprimir_todos_medicamentos(raiz);
                break;

            case 5:  // Sair
                printf("Saindo...\n");
                break;

            default:
                printf("Opção inválida.\n");
                break;
        }
    } while (opcao != 5);

    return 0;
}
