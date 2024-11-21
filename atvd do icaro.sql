create database atividade;

use atividade;

CREATE TABLE Clientes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeCompleto VARCHAR(100) NOT NULL,
    CPF CHAR(11) UNIQUE NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Telefone VARCHAR(15)
);

CREATE TABLE Funcionarios (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeCompleto VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Telefone VARCHAR(15)
);

CREATE TABLE Solicitacoes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    IDCliente INT NOT NULL,
    IDFuncionario INT,
    Descricao TEXT NOT NULL,
    Urgencia ENUM('baixa', 'média', 'alta') DEFAULT 'baixa',
    Status ENUM('pendente', 'em andamento', 'finalizada') DEFAULT 'pendente',
    DataAbertura TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (IDCliente) REFERENCES Clientes(ID),
    FOREIGN KEY (IDFuncionario) REFERENCES Funcionarios(ID)
);
