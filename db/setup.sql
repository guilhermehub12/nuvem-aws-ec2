CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(255),
    nome VARCHAR(255),
    idade INT,
    curso VARCHAR(255)
);

INSERT INTO alunos (nome, matricula, idade, curso) VALUES ('Guilherme', '12345', 21, 'Analise e Desenvolvimento de Sistemas');
INSERT INTO alunos (nome, matricula, idade, curso) VALUES ('Raquel', '12423', 24, 'Analise e Desenvolvimento de Sistemas');
INSERT INTO alunos (nome, matricula, idade, curso) VALUES ('Mozar', '12432', 23, 'Analise e Desenvolvimento de Sistemas');


CREATE TABLE IF NOT EXISTS professores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    titulo VARCHAR(255),
    curso VARCHAR(255)
);

INSERT INTO professores (nome, titulo, curso) VALUES ('Ricardo', 'Coordenador e Professor', 'Analise e Desenvolvimento de Sistemas');
INSERT INTO professores (nome, titulo, curso) VALUES ('Francisco', 'Professor', 'Analise e Desenvolvimento de Sistemas');
INSERT INTO professores (nome, titulo, curso) VALUES ('Fabricio', 'Professor', 'Analise e Desenvolvimento de Sistemas');
