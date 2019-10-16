-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-10-2019 a las 19:16:15
-- Versión del servidor: 10.1.37-MariaDB
-- Versión de PHP: 7.3.0

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
  `domicilio` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `adopcion_solicitud`
--

CREATE TABLE `adopcion_solicitud` (
  `id` int(11) NOT NULL,
  `numero_mascotas` int(11) NOT NULL,
  `razones` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `usuario_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `adopcion_solicitud`
--

INSERT INTO `adopcion_solicitud` (`id`, `numero_mascotas`, `razones`, `created_at`, `updated_at`, `usuario_id`) VALUES
(1, 1, 'porque si', '2019-10-16 15:00:34.606521', '2019-10-16 15:08:24.963552', 2),
(2, 1, 'sasas', '2019-10-16 15:08:17.957852', '2019-10-16 15:08:17.957852', 2),
(3, 2, 'dfsdfdsf', '2019-10-16 15:49:46.331664', '2019-10-16 15:49:46.331664', 2);

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
(25, 'Can add persona', 7, 'add_persona'),
(26, 'Can change persona', 7, 'change_persona'),
(27, 'Can delete persona', 7, 'delete_persona'),
(28, 'Can view persona', 7, 'view_persona'),
(29, 'Can add solicitud', 8, 'add_solicitud'),
(30, 'Can change solicitud', 8, 'change_solicitud'),
(31, 'Can delete solicitud', 8, 'delete_solicitud'),
(32, 'Can view solicitud', 8, 'view_solicitud'),
(33, 'Can add mascota', 9, 'add_mascota'),
(34, 'Can change mascota', 9, 'change_mascota'),
(35, 'Can delete mascota', 9, 'delete_mascota'),
(36, 'Can view mascota', 9, 'view_mascota'),
(37, 'Can add vacuna', 10, 'add_vacuna'),
(38, 'Can change vacuna', 10, 'change_vacuna'),
(39, 'Can delete vacuna', 10, 'delete_vacuna'),
(40, 'Can view vacuna', 10, 'view_vacuna');

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
(1, 'pbkdf2_sha256$150000$o0s4Nhp3kGUa$BBNkZacnwsBZAzcaLdxTtz60XmMaI60jCicm/t0ggVU=', '2019-10-16 16:29:53.629370', 1, 'admin', '', '', 'vituccibruno@gmail.com', 1, 1, '2019-10-16 14:56:50.952158'),
(2, 'pbkdf2_sha256$150000$5v1JkP7KlXri$wg7MXtFWELbq0lTtJ6No1UDhX2A/Knybq9AwACTKHpo=', '2019-10-16 15:00:08.514913', 0, 'ricardoalvarez', 'ricardo', 'alvarez', 'ricardoalvarez@gmail.com', 0, 1, '2019-10-16 14:58:49.020964');

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

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-10-16 14:58:49.291991', '2', 'ricardoalvarez', 1, '[{\"added\": {}}]', 4, 1),
(2, '2019-10-16 16:30:03.695377', '1', 'canina1', 1, '[{\"added\": {}}]', 10, 1),
(3, '2019-10-16 16:30:10.794086', '2', 'felina1', 1, '[{\"added\": {}}]', 10, 1);

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
(7, 'adopcion', 'persona'),
(8, 'adopcion', 'solicitud'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'mascota', 'mascota'),
(10, 'mascota', 'vacuna'),
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
(1, 'contenttypes', '0001_initial', '2019-10-16 14:53:45.824647'),
(2, 'auth', '0001_initial', '2019-10-16 14:53:46.914756'),
(3, 'admin', '0001_initial', '2019-10-16 14:53:52.821347'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-10-16 14:53:55.525617'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-10-16 14:53:55.773642'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-10-16 14:53:56.662731'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-10-16 14:53:57.687834'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-10-16 14:53:58.770942'),
(9, 'auth', '0004_alter_user_username_opts', '2019-10-16 14:53:58.818947'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-10-16 14:53:59.285993'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-10-16 14:53:59.320997'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-10-16 14:53:59.357000'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-10-16 14:54:00.186083'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-10-16 14:54:01.028168'),
(15, 'auth', '0010_alter_group_name_max_length', '2019-10-16 14:54:01.878253'),
(16, 'auth', '0011_update_proxy_permissions', '2019-10-16 14:54:01.915256'),
(17, 'sessions', '0001_initial', '2019-10-16 14:54:02.096274'),
(18, 'adopcion', '0001_initial', '2019-10-16 14:55:20.722136'),
(19, 'mascota', '0001_initial', '2019-10-16 14:55:21.983262');

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
('fkwm58o0nvfxoav7r2v9pgekxfow5jux', 'ODVmMzNlNDI4YTNiZTkxYjI1M2VhMjRjNDg3MmJjYTViZjViZjliNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MjM1ZDUxMzRlMWIyZjg3OTk2ZmE0Njk4OTA3OWY1MjFhMDMyZjAwIn0=', '2019-10-30 16:29:53.731380');

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
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `usuario_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `mascota_mascota`
--

INSERT INTO `mascota_mascota` (`id`, `nombre`, `sexo`, `edad_aproximada`, `fecha_rescate`, `created_at`, `updated_at`, `usuario_id`) VALUES
(1, 'negrita', 'femenino', 4, '2018-10-08', '2019-10-16 15:08:50.749131', '2019-10-16 16:32:29.043910', 2),
(2, 'blanquita', 'femenino', 2, '2018-10-08', '2019-10-16 15:49:33.803412', '2019-10-16 16:32:25.704576', 2);

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
(2, 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascota_vacuna`
--

CREATE TABLE `mascota_vacuna` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `mascota_vacuna`
--

INSERT INTO `mascota_vacuna` (`id`, `nombre`, `created_at`, `updated_at`) VALUES
(1, 'canina1', '2019-10-16 16:30:03.613368', '2019-10-16 16:30:03.613368'),
(2, 'felina1', '2019-10-16 16:30:10.780085', '2019-10-16 16:30:10.780085');

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
  ADD KEY `adopcion_solicitud_usuario_id_167615d1_fk_auth_user_id` (`usuario_id`);

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
  ADD KEY `mascota_mascota_usuario_id_3cae744e_fk_auth_user_id` (`usuario_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `adopcion_solicitud`
--
ALTER TABLE `adopcion_solicitud`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `mascota_mascota`
--
ALTER TABLE `mascota_mascota`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `mascota_mascota_vacuna`
--
ALTER TABLE `mascota_mascota_vacuna`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
  ADD CONSTRAINT `adopcion_solicitud_usuario_id_167615d1_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);

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
  ADD CONSTRAINT `mascota_mascota_usuario_id_3cae744e_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);

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
