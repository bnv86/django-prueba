-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-10-2019 a las 06:05:45
-- Versión del servidor: 10.1.26-MariaDB
-- Versión de PHP: 7.0.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `refugio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `adopcion_persona`
--

CREATE TABLE `adopcion_persona` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(70) NOT NULL,
  `edad` int(11) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `email` varchar(254) NOT NULL,
  `domicilio` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `adopcion_persona`
--

INSERT INTO `adopcion_persona` (`id`, `nombre`, `apellido`, `edad`, `telefono`, `email`, `domicilio`) VALUES
(1, 'Ricardo', 'Alvarez', 53, '123456', 'ricardo@gmail.com', 'casa'),
(2, 'Yolanda', 'Bianchi', 59, '987654', 'yolanda@gmail.com', 'casa'),
(4, 'Bruno', 'Vitucci', 32, '1234', 'vituccibruno@gmail.com', 'casa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `adopcion_solicitud`
--

CREATE TABLE `adopcion_solicitud` (
  `id` int(11) NOT NULL,
  `numero_mascotas` int(11) NOT NULL,
  `razones` longtext NOT NULL,
  `persona_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `adopcion_solicitud`
--

INSERT INTO `adopcion_solicitud` (`id`, `numero_mascotas`, `razones`, `persona_id`) VALUES
(1, 2, 'quiero dos gatitos nuevos', 4),
(2, 3, 'fsdfsdfds', NULL),
(3, 3, 'quiero cuidar mi hogar', NULL),
(4, 3, 'quiero 3 doguis', NULL),
(5, 2, 'asdasdasd', NULL),
(10, 1, 'dxadas d', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add vacuna', 7, 'add_vacuna'),
(26, 'Can change vacuna', 7, 'change_vacuna'),
(27, 'Can delete vacuna', 7, 'delete_vacuna'),
(28, 'Can view vacuna', 7, 'view_vacuna'),
(29, 'Can add mascota', 8, 'add_mascota'),
(30, 'Can change mascota', 8, 'change_mascota'),
(31, 'Can delete mascota', 8, 'delete_mascota'),
(32, 'Can view mascota', 8, 'view_mascota'),
(33, 'Can add persona', 9, 'add_persona'),
(34, 'Can change persona', 9, 'change_persona'),
(35, 'Can delete persona', 9, 'delete_persona'),
(36, 'Can view persona', 9, 'view_persona'),
(37, 'Can add solicitud', 10, 'add_solicitud'),
(38, 'Can change solicitud', 10, 'change_solicitud'),
(39, 'Can delete solicitud', 10, 'delete_solicitud'),
(40, 'Can view solicitud', 10, 'view_solicitud');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$8bouJNTTAJAo$c1iFU3DMcOMGZIxx2PkyyJLvMVdA6VvGRmJ40yNlM5k=', '2019-10-08 04:04:39.881804', 1, 'admin', '', '', 'vituccibruno@gmail.com', 1, 1, '2019-09-29 22:42:33.381448'),
(2, 'pbkdf2_sha256$150000$16SCqzT9m4BY$wAyt0GLAolkUmVLsMo1QoWwbH886boLUKZOO0e3/A8A=', NULL, 0, 'jorge18', '', '', '', 0, 1, '2019-10-07 21:45:25.957354'),
(3, 'pbkdf2_sha256$150000$c45DgJCt2VXD$Q79AuerGUFVQMOSVu4QiroQX/ST3CmiZY2wQL1YkHpM=', NULL, 0, 'jorge20', '', '', '', 0, 1, '2019-10-07 21:46:10.180883'),
(4, 'pbkdf2_sha256$150000$9JFfvbqCOb0V$wyoDgLCqjL/9ZhiyCNV0POdmKbU1Om9EehlafcUYmuQ=', NULL, 0, 'marchu', 'martin', 'rodriguez', 'mrodri@gmail.com', 0, 1, '2019-10-08 02:39:00.437844'),
(5, 'pbkdf2_sha256$150000$R1o93KiM1CG0$b+VGlE6SWrL3w0k1bgwcet4vALDTe7dwWNMNxkvG1PI=', '2019-10-08 04:04:22.081786', 0, 'carlitos', 'carlos', 'mendoza', 'cmendoza@gmail.com', 0, 1, '2019-10-08 03:44:25.419341');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(9, 'adopcion', 'persona'),
(10, 'adopcion', 'solicitud'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'mascota', 'mascota'),
(7, 'mascota', 'vacuna'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-09-29 22:41:32.923990'),
(2, 'auth', '0001_initial', '2019-09-29 22:41:34.812098'),
(3, 'admin', '0001_initial', '2019-09-29 22:41:43.580599'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-09-29 22:41:45.117687'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-09-29 22:41:45.232694'),
(6, 'adopcion', '0001_initial', '2019-09-29 22:41:45.599715'),
(7, 'contenttypes', '0002_remove_content_type_name', '2019-09-29 22:41:46.671776'),
(8, 'auth', '0002_alter_permission_name_max_length', '2019-09-29 22:41:47.561827'),
(9, 'auth', '0003_alter_user_email_max_length', '2019-09-29 22:41:48.772896'),
(10, 'auth', '0004_alter_user_username_opts', '2019-09-29 22:41:48.829899'),
(11, 'auth', '0005_alter_user_last_login_null', '2019-09-29 22:41:49.411933'),
(12, 'auth', '0006_require_contenttypes_0002', '2019-09-29 22:41:49.442935'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2019-09-29 22:41:49.487937'),
(14, 'auth', '0008_alter_user_username_max_length', '2019-09-29 22:41:50.821013'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2019-09-29 22:41:52.149089'),
(16, 'auth', '0010_alter_group_name_max_length', '2019-09-29 22:41:53.590172'),
(17, 'auth', '0011_update_proxy_permissions', '2019-09-29 22:41:53.732180'),
(18, 'mascota', '0001_initial', '2019-09-29 22:41:54.352215'),
(19, 'sessions', '0001_initial', '2019-09-29 22:41:57.147375'),
(20, 'adopcion', '0002_solicitud', '2019-10-04 05:46:58.999408');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('pv13bomf2bbpf5mgzodyaavfniou6kms', 'NzQxNmVkMTg1NzFlMDBmYzE0NWU5YjAwNDVjMmNiMTJlOWQ0NWI0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNDExZGNhMjE5NzQ2YWNjNjFhNDAxYWRkZTZiOTkyN2MyYzM3NjZjIn0=', '2019-10-22 04:04:39.983810'),
('qpvpr3crzng8gdl6pm4iqlq9dhdk7nvf', 'MDJiMjc1NzFlNjI3NDk2NzVkNTk5N2RkYmMxMTRkZDYzN2YzMDI0Zjp7fQ==', '2019-10-22 04:03:44.397630'),
('vebkjkkxj3n1gjyk1rjcmwq8jpmhlwqx', 'NzQxNmVkMTg1NzFlMDBmYzE0NWU5YjAwNDVjMmNiMTJlOWQ0NWI0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNDExZGNhMjE5NzQ2YWNjNjFhNDAxYWRkZTZiOTkyN2MyYzM3NjZjIn0=', '2019-10-13 22:49:35.359583');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascota_mascota`
--

CREATE TABLE `mascota_mascota` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `edad_aproximada` int(11) NOT NULL,
  `fecha_rescate` date NOT NULL,
  `persona_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `mascota_mascota`
--

INSERT INTO `mascota_mascota` (`id`, `nombre`, `sexo`, `edad_aproximada`, `fecha_rescate`, `persona_id`) VALUES
(1, 'tete', 'macho', 2, '2018-09-02', 2),
(3, 'pipo', 'macho', 8, '2019-08-02', 1),
(4, 'claudia caniggia', 'hembra', 25, '2017-10-02', 2),
(5, 'vaquita', 'hembra', 2, '2016-10-02', 2),
(6, 'minina', 'hembra', 2, '2016-10-02', 2),
(9, 'la gatita', 'hembra', 5, '2019-08-02', 1),
(10, 'fray', 'macho', 6, '2013-10-15', 2),
(11, 'pepim', 'macho', 6, '2013-10-15', 4),
(13, 'zarco', 'macho', 10, '2003-09-02', 1),
(16, 'ch', 'hembra', 2, '2003-09-02', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascota_mascota_vacuna`
--

CREATE TABLE `mascota_mascota_vacuna` (
  `id` int(11) NOT NULL,
  `mascota_id` int(11) NOT NULL,
  `vacuna_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `mascota_mascota_vacuna`
--

INSERT INTO `mascota_mascota_vacuna` (`id`, `mascota_id`, `vacuna_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(4, 3, 1),
(5, 4, 2),
(9, 5, 1),
(6, 5, 2),
(7, 6, 2),
(8, 11, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascota_vacuna`
--

CREATE TABLE `mascota_vacuna` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `mascota_vacuna`
--

INSERT INTO `mascota_vacuna` (`id`, `nombre`) VALUES
(1, 'canina 1'),
(2, 'felina 1');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `adopcion_persona`
--
ALTER TABLE `adopcion_persona`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `adopcion_solicitud`
--
ALTER TABLE `adopcion_solicitud`
  ADD PRIMARY KEY (`id`),
  ADD KEY `adopcion_solicitud_persona_id_3618c7a5_fk_adopcion_persona_id` (`persona_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `mascota_mascota`
--
ALTER TABLE `mascota_mascota`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mascota_mascota_persona_id_b662f6c9_fk_adopcion_persona_id` (`persona_id`);

--
-- Indices de la tabla `mascota_mascota_vacuna`
--
ALTER TABLE `mascota_mascota_vacuna`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mascota_mascota_vacuna_mascota_id_vacuna_id_346591c7_uniq` (`mascota_id`,`vacuna_id`),
  ADD KEY `mascota_mascota_vacuna_vacuna_id_a8a1dd12_fk_mascota_vacuna_id` (`vacuna_id`);

--
-- Indices de la tabla `mascota_vacuna`
--
ALTER TABLE `mascota_vacuna`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `adopcion_persona`
--
ALTER TABLE `adopcion_persona`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `adopcion_solicitud`
--
ALTER TABLE `adopcion_solicitud`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `mascota_mascota`
--
ALTER TABLE `mascota_mascota`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `mascota_mascota_vacuna`
--
ALTER TABLE `mascota_mascota_vacuna`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `mascota_vacuna`
--
ALTER TABLE `mascota_vacuna`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `adopcion_solicitud`
--
ALTER TABLE `adopcion_solicitud`
  ADD CONSTRAINT `adopcion_solicitud_persona_id_3618c7a5_fk_adopcion_persona_id` FOREIGN KEY (`persona_id`) REFERENCES `adopcion_persona` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `mascota_mascota`
--
ALTER TABLE `mascota_mascota`
  ADD CONSTRAINT `mascota_mascota_persona_id_b662f6c9_fk_adopcion_persona_id` FOREIGN KEY (`persona_id`) REFERENCES `adopcion_persona` (`id`);

--
-- Filtros para la tabla `mascota_mascota_vacuna`
--
ALTER TABLE `mascota_mascota_vacuna`
  ADD CONSTRAINT `mascota_mascota_vacuna_mascota_id_b0fc0568_fk_mascota_mascota_id` FOREIGN KEY (`mascota_id`) REFERENCES `mascota_mascota` (`id`),
  ADD CONSTRAINT `mascota_mascota_vacuna_vacuna_id_a8a1dd12_fk_mascota_vacuna_id` FOREIGN KEY (`vacuna_id`) REFERENCES `mascota_vacuna` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
