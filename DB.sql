-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema Pandas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Pandas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Pandas` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `Pandas` ;

-- -----------------------------------------------------
-- Table `Pandas`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Pandas`.`Clientes` (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(15) NULL DEFAULT NULL,
  `direccion` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE INDEX `email` (`email` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `Pandas`.`Proveedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Pandas`.`Proveedores` (
  `id_proveedor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `contacto` VARCHAR(100) NULL DEFAULT NULL,
  `telefono` VARCHAR(15) NULL DEFAULT NULL,
  `direccion` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id_proveedor`))
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `Pandas`.`Compras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Pandas`.`Compras` (
  `id_compra` INT NOT NULL AUTO_INCREMENT,
  `id_proveedor` INT NULL DEFAULT NULL,
  `fecha` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `total` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id_compra`),
  INDEX `id_proveedor` (`id_proveedor` ASC) VISIBLE,
  CONSTRAINT `Compras_ibfk_1`
    FOREIGN KEY (`id_proveedor`)
    REFERENCES `Pandas`.`Proveedores` (`id_proveedor`))
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `Pandas`.`Productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Pandas`.`Productos` (
  `id_producto` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `descripcion` TEXT NULL DEFAULT NULL,
  `precio` DECIMAL(10,2) NOT NULL,
  `stock` INT NOT NULL,
  `categoria` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id_producto`))
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `Pandas`.`DetallesCompra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Pandas`.`DetallesCompra` (
  `id_detalle_compra` INT NOT NULL AUTO_INCREMENT,
  `id_compra` INT NULL DEFAULT NULL,
  `id_producto` INT NULL DEFAULT NULL,
  `cantidad` INT NOT NULL,
  `precio_unitario` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id_detalle_compra`),
  INDEX `id_compra` (`id_compra` ASC) VISIBLE,
  INDEX `id_producto` (`id_producto` ASC) VISIBLE,
  CONSTRAINT `DetallesCompra_ibfk_1`
    FOREIGN KEY (`id_compra`)
    REFERENCES `Pandas`.`Compras` (`id_compra`),
  CONSTRAINT `DetallesCompra_ibfk_2`
    FOREIGN KEY (`id_producto`)
    REFERENCES `Pandas`.`Productos` (`id_producto`))
ENGINE = InnoDB
AUTO_INCREMENT = 28
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `Pandas`.`Ordenes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Pandas`.`Ordenes` (
  `id_orden` INT NOT NULL AUTO_INCREMENT,
  `id_cliente` INT NULL DEFAULT NULL,
  `fecha` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `total` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id_orden`),
  INDEX `id_cliente` (`id_cliente` ASC) VISIBLE,
  CONSTRAINT `Ordenes_ibfk_1`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `Pandas`.`Clientes` (`id_cliente`))
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `Pandas`.`DetallesOrden`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Pandas`.`DetallesOrden` (
  `id_detalle` INT NOT NULL AUTO_INCREMENT,
  `id_orden` INT NULL DEFAULT NULL,
  `id_producto` INT NULL DEFAULT NULL,
  `cantidad` INT NOT NULL,
  `precio_unitario` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id_detalle`),
  INDEX `id_orden` (`id_orden` ASC) VISIBLE,
  INDEX `id_producto` (`id_producto` ASC) VISIBLE,
  CONSTRAINT `DetallesOrden_ibfk_1`
    FOREIGN KEY (`id_orden`)
    REFERENCES `Pandas`.`Ordenes` (`id_orden`),
  CONSTRAINT `DetallesOrden_ibfk_2`
    FOREIGN KEY (`id_producto`)
    REFERENCES `Pandas`.`Productos` (`id_producto`))
ENGINE = InnoDB
AUTO_INCREMENT = 28
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
