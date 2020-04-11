drop database starcraft;
create database starcraft; 
\connect starcraft;

create schema datapack;
create schema replay;
create schema events;

-- +
create table datapack.unit_type
(
	__id__				integer,
	id 				integer,
	version				varchar(100),
	str_id 				varchar(100),
	name  				varchar(100),
	title  				varchar(100),
	race 				varchar(100),
	minerals			integer,
	vespene				integer,
	supply				integer,
	is_building 			boolean,
	is_worker			boolean,
	is_army				boolean,
	PRIMARY KEY (__id__)
);

-- +
create table datapack.ability
(
	__id__				integer,
	id				integer,
	version				varchar(100),
 	name				varchar(100),
 	title 				varchar(100),
 	is_build			boolean,
 	build_time			integer,
 	build_unit			integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (build_unit) REFERENCES datapack.unit_type(__id__)
);

-- +
create table replay.info 
(

	__id__				serial,
	filename                	varchar(100),
	filehash                	varchar(100),
	load_level              	integer,
	speed           		varchar(100),
	type            		varchar(100),
	game_type               	varchar(100),
	real_type               	varchar(100),
	category                	varchar(100),
	is_ladder               	boolean,
	is_private              	boolean,
	map_hash                	varchar(100),
	region          		varchar(100),
	game_fps                	real,
	frames          		integer,
	build           		integer,
	base_build              	integer,
	release_string          	varchar(100),
	amm             		integer,
	competitive             	integer,
	practice                	integer,
	cooperative             	integer,
	battle_net              	integer,
	hero_duplicates_allowed         integer,
	map_name                	varchar(100),
	expansion               	varchar(100),
	windows_timestamp               integer,
	unix_timestamp          	integer,
	end_time                	timestamp,
	time_zone               	real,
	start_time              	timestamp,
	date            		timestamp,
	winner         			integer 
	people_hash             	varchar(100),
	PRIMARY KEY (__id__),
	FOREIGN KEY (winner) REFERENCES replay.player(__id__)
);


create table replay.player
(
	__id__				serial,
	sid             		integer,
	team_id         		integer,
	is_human                	boolean,
	is_observer             	boolean,
	is_referee              	boolean,
	region          		varchar(100),
	subregion               	integer,
	toon_id         		integer,
	uid             		integer,
	-- -- init_data good for scaled_rating
	-- init_data               <class 'dict'>
	clan_tag                	varchar(100),
	name            		varchar(100),
	combined_race_levels            integer,
	highest_league          	integer,
	pid             		integer,
	-- -- detail_data dictionary may be useful for player ID info
	-- detail_data             <class 'dict'>
	result          		varchar(100),
	pick_race               	varchar(100),
	play_race               	varchar(100),
	replay_id			integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (replay_id) REFERENCES replay.info(__id__)
);

create table events.PlayerSetupEvent
(
	__id__				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	pid             		integer,
	type            		integer,
	uid             		integer,
	sid             		integer
	
);

create table events.UpgradeCompleteEvent
(
	__id__				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	pid             		integer,
	player          		integer,
	upgrade_type_name               varchar(100),
	count           		integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__)
);

create table events.UnitBornEvent
(
	__id__				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	unit_id_index           	integer,
	unit_id_recycle         	integer,
	unit_id         		integer,
	unit            		integer,
	unit_type_name          	varchar(100),
	control_pid             	integer,
	upkeep_pid              	integer,
	unit_upkeeper           	integer,
	unit_controller         	integer,
	x               		integer,
	y               		integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (unit) REFERENCES datapack.unit_type(__id__)
	FOREIGN KEY (unit_upkeeper) REFERENCES replay.player(__id__)
	FOREIGN KEY (unit_controller) REFERENCES replay.player(__id__)
	
);

create table events.ProgressEvent
(
	__id__				serial,
	pid             		integer,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	progress                	integer,
	player          		integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__)
);

create table events.PlayerStatsEvent
(
	__id__					serial,
	frame           			integer,
	second          			integer,
	name            			varchar(100),
	pid             			integer,
	player          			integer,
	minerals_current                	integer,
	vespene_current         		integer,
	minerals_collection_rate        	integer,
	vespene_collection_rate         	integer,
	workers_active_count            	integer,
	minerals_used_in_progress_army  	integer,
	minerals_used_in_progress_economy       integer,
	minerals_used_in_progress_technology    integer,
	minerals_used_in_progress               integer,
	vespene_used_in_progress_army           integer,
	vespene_used_in_progress_economy        integer,
	vespene_used_in_progress_technology     integer,
	vespene_used_in_progress                integer,
	resources_used_in_progress              integer,
	minerals_used_current_army              integer,
	minerals_used_current_economy           integer,
	minerals_used_current_technology        integer,
	minerals_used_current           	integer,
	vespene_used_current_army               integer,
	vespene_used_current_economy            integer,
	vespene_used_current_technology         integer,
	vespene_used_current            	integer,
	resources_used_current          	integer,
	minerals_lost_army              	integer,
	minerals_lost_economy           	integer,
	minerals_lost_technology                integer,
	minerals_lost           		integer,
	vespene_lost_army               	integer,
	vespene_lost_economy            	integer,
	vespene_lost_technology         	integer,
	vespene_lost            		integer,
	resources_lost          		integer,
	minerals_killed_army            	integer,
	minerals_killed_economy         	integer,
	minerals_killed_technology              integer,
	minerals_killed         		integer,
	vespene_killed_army             	integer,
	vespene_killed_economy          	integer,
	vespene_killed_technology               integer,
	vespene_killed          		integer,
	resources_killed                	integer,
	food_used               		real,
	food_made               		real,
	minerals_used_active_forces             integer,
	vespene_used_active_forces              integer,
	ff_minerals_lost_army           	integer,
	ff_minerals_lost_economy                integer,
	ff_minerals_lost_technology             integer,
	ff_vespene_lost_army            	integer,
	ff_vespene_lost_economy         	integer,
	ff_vespene_lost_technology              integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__)
);

create table events.CameraEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local               		boolean,
	name            		varchar(100),
	x               		real,
	y               		real,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__)
);

create table events.SelectionEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local               	  	boolean,
	name            		varchar(100),
	control_group           	integer,
	bank            		integer,
	subgroup_index          	integer,
	mask_type               	varchar(100),
	-- -- mask_data               	<class 'NoneType'>,
	-- -- new_unit_types          	<class 'list'>,
	-- -- new_unit_ids            	<class 'list'>,
	-- -- new_unit_info           	<class 'list'>,
	-- -- new_units               	<class 'list'>,
	-- -- objects         		<class 'list'>,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__)
);

create table events.BasicCommandEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local                	boolean,
	name            		varchar(100),
	flags           		integer,
	-- -- flag            		<class 'dict'>,
	has_ability             	boolean,
	ability_link            	integer,
	command_index           	integer,
	-- -- ability_data            	<class 'NoneType'>,
	ability_id              	integer,
	ability         		integer,
	ability_name            	varchar(100),
	ability_type            	varchar(100),
	-- -- ability_type_data               <class 'NoneType'>,
	-- -- other_unit_id           	<class 'NoneType'>,
	-- -- other_unit              	<class 'NoneType'>,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__),
	FOREIGN KEY (ability) REFERENCES datapack.ability(__id__)
);

create table events.TargetPointCommandEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local                	boolean,
	name            		varchar(100),
	flags           		integer,
	-- -- flag            		<class 'dict'>,
	has_ability             	boolean,
	ability_link            	integer,
	command_index           	integer,
	ability_data            	integer,
	ability_id              	integer,
	ability         		integer,
	ability_name            	varchar(100),
	ability_type            	varchar(100),
	-- -- ability_type_data               <class 'dict'>,
	-- -- other_unit_id           	<class 'NoneType'>,
	-- -- other_unit              	<class 'NoneType'>,
	x               		real,
	y               		real,
	z               		integer,
	-- -- location                	<class 'tuple'>,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__),
	FOREIGN KEY (ability) REFERENCES datapack.ability(__id__)
);

create table events.ControlGroupEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local                	boolean,
	name            		varchar(100),
	control_group           	integer,
	bank            		integer,
	hotkey          		integer,
	update_type             	integer,
	mask_type               	varchar(100),
	-- -- mask_data               	<class 'NoneType'>,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__)
);

create table events.ChatEvent
(
	__id__				serial,
	pid             		integer,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	target          		integer,
	text            		varchar(100),
	to_all          		boolean,
	to_allies               	boolean,
	to_observers            	boolean,
	player          		integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__)
);

create table events.UpdateTargetPointCommandEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local                	boolean,
	name            		varchar(100),
	flags           		integer,
	-- -- flag            		<class 'dict'>,
	has_ability             	boolean,
	ability_link            	integer,
	command_index           	integer,
	ability_data            	integer,
	ability_id              	integer,
	ability         		integer,
	ability_name            	varchar(100),
	ability_type            	varchar(100),
	-- -- ability_type_data               <class 'dict'>,
	-- -- other_unit_id           	<class 'NoneType'>,
	-- -- other_unit              	<class 'NoneType'>,
	x               		real,
	y               		real,
	z               		integer,
	-- -- location                	<class 'tuple'>,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__),
	FOREIGN KEY (ability) REFERENCES datapack.ability(__id__)
);

create table events.GetControlGroupEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local                	boolean,
	name            		varchar(100),
	control_group           	integer,
	bank            		integer,
	hotkey          		integer,
	update_type             	integer,
	mask_type               	varchar(100),
	-- -- mask_data               	<class 'NoneType'>,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__)
);

create table events.TargetUnitCommandEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local                	boolean,
	name            		varchar(100),
	flags           		integer,
	-- -- flag            		<class 'dict'>,
	has_ability             	boolean,
	ability_link            	integer,
	command_index           	integer,
	ability_data            	integer,
	ability_id              	integer,
	ability         		integer,
	ability_name            	varchar(100),
	ability_type            	varchar(100),
	-- -- ability_type_data               <class 'dict'>,
	-- -- other_unit_id           	<class 'NoneType'>,
	-- -- other_unit              	<class 'NoneType'>,
	target_flags            	integer,
	target_timer            	integer,
	target_unit_id          	integer,
	-- -- target_unit             	<class 'NoneType'>,
	target_unit_type                integer,
	control_player_id               integer,
	upkeep_player_id                integer,
	x               		real,
	y               		real,
	z               		integer,
	-- -- location                	<class 'tuple'>,
	target          		integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__),
	FOREIGN KEY (ability) REFERENCES datapack.ability(__id__),
	FOREIGN KEY (target) REFERENCES datapack.unit_type(__id__)
);

create table events.UnitInitEvent
(
	__id__				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	unit_id_index           	integer,
	unit_id_recycle         	integer,
	unit_id         		integer,
	unit            		integer,
	unit_type_name          	varchar(100),
	control_pid             	integer,
	upkeep_pid              	integer,
	unit_upkeeper           	integer,
	unit_controller         	integer,
	x               		integer,
	y               		integer,
	-- -- location                	<class 'tuple'>,
	PRIMARY KEY (__id__),
	FOREIGN KEY (unit_controller) REFERENCES replay.player(__id__),
	FOREIGN KEY (unit_upkeeper) REFERENCES replay.player(__id__),
	FOREIGN KEY (unit) REFERENCES datapack.unit_type(__id__)
);

create table events.SetControlGroupEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local                	boolean,
	name            		varchar(100),
	control_group           	integer,
	bank            		integer,
	hotkey          		integer,
	update_type             	integer,
	mask_type               	varchar(100),
	-- -- mask_data               	<class 'NoneType'>,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__)
);

create table events.UnitDoneEvent
(
	__id__				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	unit_id_index           	integer,
	unit_id_recycle         	integer,
	unit_id         		integer,
	unit            		integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (unit) REFERENCES datapack.unit_type(__id__)
	
);

create table events.UpdateTargetUnitCommandEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local        		        boolean,
	name            		varchar(100),
	flags           		integer,
	-- -- flag            		<class 'dict'>,
	has_ability             	boolean,
	ability_link            	integer,
	command_index           	integer,
	ability_data            	integer,
	ability_id              	integer,
	ability         		integer,
	ability_name            	varchar(100),
	ability_type            	varchar(100),
	-- -- ability_type_data              	<class 'dict'>,
	-- -- other_unit_id           	<class 'NoneType'>,
	-- -- other_unit              	<class 'NoneType'>,
	target_flags            	integer,
	target_timer            	integer,
	target_unit_id          	integer,
	-- -- target_unit             	<class 'NoneType'>,
	target_unit_type                integer,
	control_player_id               integer,
	upkeep_player_id                integer,
	x               		real,
	y               		real,
	z               		integer,
	-- -- location        		<class 'tuple'>,
	target          		integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__),
	FOREIGN KEY (ability) REFERENCES datapack.ability(__id__),
	FOREIGN KEY (target) REFERENCES datapack.unit_type(__id__)
);

create table events.UnitTypeChangeEvent
(
	__id__				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	unit_id_index           	integer,
	unit_id_recycle         	integer,
	unit_id         		integer,
	unit            		integer,
	unit_type_name          	varchar(100),
	PRIMARY KEY (__id__),
	FOREIGN KEY (unit) REFERENCES datapack.unit_type(__id__)
);

create table events.UnitDiedEvent
(
	__id__				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	unit_id_index           	integer,
	unit_id_recycle         	integer,
	unit_id         		integer,
	unit            		integer,
	killer_pid              	integer,
	killer          		integer,
	killing_player_id               integer,
	killing_player          	integer,
	x               		integer,
	y               		integer,
	-- -- location                	<class 'tuple'>,
	killing_unit_index              integer,
	killing_unit_recycle            integer,
	killing_unit_id         	integer,
	killing_unit            	integer,
	PRIMARY KEY (__id__),
	FOREIGN KEY (killer) REFERENCES replay.player(__id__),
	FOREIGN KEY (killing_player) REFERENCES replay.player(__id__),
	FOREIGN KEY (unit) REFERENCES datapack.unit_type(__id__),
	FOREIGN KEY (killing_unit) REFERENCES datapack.unit_type(__id__)
);

create table events.UnitPositionsEvent
(
	__id__				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	first_unit_index                integer,
	-- -- items           		<class 'list'>,
	-- -- units           		<class 'dict'>,
	-- -- positions               	<class 'list'>,
	PRIMARY KEY (__id__)
);

create table events.PlayerLeaveEvent
(
	__id__				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local                	boolean,
	name            		varchar(100),
	-- -- data            		<class 'dict'>,
	PRIMARY KEY (__id__),
	FOREIGN KEY (player) REFERENCES replay.player(__id__)
);
