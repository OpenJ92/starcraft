drop database starcraft;
create database starcraft; 
\connect starcraft;

create schema datapack;
create schema replay;
create schema events;

create table datapack.unit_type
(
	iid				integer,
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
	PRIMARY KEY (iid)
);

create table datapack.ability
(
	iid				integer,
	id				integer,
	version				varchar(100),
 	name				varchar(100),
 	title 				varchar(100),
 	is_build			boolean,
 	build_time			integer,
 	build_unit			integer,
	PRIMARY KEY (iid),
	FOREIGN KEY (build_unit) REFERENCES datapack.unit_type(iid)
);

create table replay.player
(
	iid				serial,
	sid             		integer,
	-- slot_data               <class 'dict'>
	handicap                	integer,
	team_id         		integer,
	is_human                	boolean,
	is_observer             	boolean,
	is_referee              	boolean,
	hero_name               	varchar(100),
	hero_skin               	varchar(100),
	hero_mount              	varchar(100),
	toon_handle             	varchar(100),
	region          		varchar(100),
	subregion               	integer,
	toon_id         		integer,
	-- events          <class 'list'>
	-- messages                <class 'list'>
	uid             		integer,
	-- init_data               <class 'dict'>
	clan_tag                	varchar(100),
	name            		varchar(100),
	combined_race_levels            integer,
	highest_league          	integer,
	-- recorder                <class 'NoneType'>
	pid             		integer,
	-- detail_data             <class 'dict'>
	-- attribute_data          <class 'dict'>
	result          		varchar(100),
	-- team            <class 'sc2reader.objects.Team'>
	pick_race               	varchar(100),
	difficulty              	varchar(100),
	play_race               	varchar(100),
	commander               	varchar(100),
	commander_level         	integer,
	-- commander_mastery_level         <class 'list'>
	trophy_id               	integer,
	-- commander_mastery_talents               <class 'list'>
	-- color           <class 'sc2reader.utils.Color'>
	-- units           <class 'list'>
	-- killed_units            <class 'list'>
	PRIMARY KEY (iid)
);

create table replay.info 
(

	-- factory         <class 'sc2reader.factories.sc2factory.SC2Factory'>
	-- opt             <class 'dict'>
	-- logger          <class 'logging.Logger'>
	filename                varchar(100),
	filehash                varchar(100),
	-- datapack                <class 'sc2reader.data.Build'>
	-- raw_data                <class 'dict'>
	load_level              integer,
	speed           varchar(100),
	type            varchar(100),
	game_type               varchar(100),
	real_type               varchar(100),
	category                varchar(100),
	is_ladder               <class 'bool'>
	is_private              <class 'bool'>
	-- map             <class 'NoneType'>
	map_hash                varchar(100),
	region          varchar(100),
	-- events          <class 'list'>
	-- teams           <class 'list'>
	-- team            <class 'dict'>
	-- player          <class 'dict'>
	-- observer                <class 'dict'>
	-- human           <class 'dict'>
	-- computer                <class 'dict'>
	-- entity          <class 'dict'>
	-- players         <class 'list'>
	-- observers               <class 'list'>
	-- humans          <class 'list'>
	-- computers               <class 'list'>
	-- entities                <class 'list'>
	-- attributes              <class 'collections.defaultdict'>
	-- messages                <class 'list'>
	-- recorder                <class 'NoneType'>
	-- packets         <class 'list'>
	-- objects         <class 'dict'>
	-- active_units            <class 'dict'>
	game_fps                real,
	-- tracker_events          <class 'list'>
	-- game_events             <class 'list'>
	-- registered_readers              <class 'collections.defaultdict'>
	-- registered_datapacks            <class 'list'>
	-- archive         <class 'mpyq.MPQArchive'>
	-- versions                <class 'list'>
	frames          integer,
	build           integer,
	base_build              integer,
	release_string          varchar(100),
	-- length          <class 'sc2reader.utils.Length'>
	-- game_length             <class 'sc2reader.utils.Length'>
	-- real_length             <class 'sc2reader.utils.Length'>
	amm             integer,
	-- ranked          <class 'NoneType'>
	competitive             integer,
	practice                integer,
	cooperative             integer,
	battle_net              integer,
	hero_duplicates_allowed         integer,
	map_name                varchar(100),
	-- map_file                <class 'sc2reader.utils.DepotFile'>
	expansion               varchar(100),
	windows_timestamp               integer,
	unix_timestamp          integer,
	end_time                timestamp,
	time_zone               real,
	start_time              timestamp,
	date            timestamp,
	-- pings           <class 'list'>
	-- message_events          <class 'list'>
	-- clients         <class 'list'>
	-- client          <class 'dict'>
	winner          <class 'sc2reader.objects.Team'>
	-- people          <class 'list'>
	-- person          <class 'dict'>
	people_hash             varchar(100),
	-- plugin_result           <class 'dict'>
	-- plugins         <class 'dict'>
	-- plugin_failures         <class 'list'>
	-- units           <class 'set'>
	-- unit            <class 'dict'>
);

create table replay.unit
(
	iid				serial,
	owner                   	<class 'sc2reader.objects.Participant'>,
	started_at                      integer,
	finished_at                     integer,
	died_at                 	<class 'NoneType'>,
	killed_by                       <class 'NoneType'>,
	killing_player                  <class 'NoneType'>,
	killing_unit                    <class 'NoneType'>,
	-- killed_units                    <class 'list'>,
	id                      	integer,
	_type_class                     integer,
	-- type_history                    <class 'collections.OrderedDict'>,
	hallucinated                    boolean,
	flags                   	integer,
	location                        <class 'tuple'>,
	PRIMARY KEY (iid),
	FOREIGN KEY (_type_class) REFERENCES datapack.unit_type(iid)
);

create table events.PlayerSetupEvent
(
	iid				serial,
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
	iid				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	pid             		integer,
	player          		integer,
	upgrade_type_name               varchar(100),
	count           		integer,
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);

create table events.UnitBornEvent
(
	iid				serial,
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
	-- -- -- unit_upkeeper           	<class 'NoneType'>,
	-- -- -- unit_controller         	<class 'NoneType'>,
	x               		integer,
	y               		integer,
	PRIMARY KEY (iid),
	FOREIGN KEY (unit) REFERENCES datapack.unit_type(iid)
	
);

create table events.ProgressEvent
(
	iid				serial,
	pid             		integer,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	progress                	integer,
	player          		integer,
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);

create table events.UserOptionsEvent
(
	iid				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local               		boolean,
	name            		varchar(100),
	game_fully_downloaded           integer,
	development_cheats_enabled      integer,
	multiplayer_cheats_enabled      integer,
	sync_checksumming_enabled       integer,
	is_map_to_map_transition        integer,
	-- -- -- use_ai_beacons          	<class 'NoneType'>,
	-- -- -- starting_rally          	<class 'NoneType'>,
	debug_pause_enabled             integer,
	base_build_num          	integer,
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);

create table events.PlayerStatsEvent
(
	iid					serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);

create table events.CameraEvent
(
	iid				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local               		boolean,
	name            		varchar(100),
	x               		real,
	y               		real,
	-- -- location                	<class 'tuple'>,
	-- -- distance                	<class 'NoneType'>,
	-- -- pitch           		<class 'NoneType'>,
	-- -- yaw             		<class 'NoneType'>,
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);

create table events.SelectionEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);

create table events.BasicCommandEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid),
	FOREIGN KEY (ability) REFERENCES datapack.ability(iid)
);

create table events.TargetPointCommandEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid),
	FOREIGN KEY (ability) REFERENCES datapack.ability(iid)
);

create table events.ControlGroupEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);

create table events.ChatEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);

create table events.UpdateTargetPointCommandEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid),
	FOREIGN KEY (ability) REFERENCES datapack.ability(iid)
);

create table events.GetControlGroupEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);

create table events.TargetUnitCommandEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid),
	FOREIGN KEY (ability) REFERENCES datapack.ability(iid),
	FOREIGN KEY (target) REFERENCES datapack.unit_type(iid)
);

create table events.UnitInitEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (unit_controller) REFERENCES replay.player(iid),
	FOREIGN KEY (unit_upkeeper) REFERENCES replay.player(iid),
	FOREIGN KEY (unit) REFERENCES datapack.unit_type(iid)
);

create table events.SetControlGroupEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);

create table events.UnitDoneEvent
(
	iid				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	unit_id_index           	integer,
	unit_id_recycle         	integer,
	unit_id         		integer,
	unit            		integer,
	PRIMARY KEY (iid),
	FOREIGN KEY (unit) REFERENCES datapack.unit_type(iid)
	
);

create table events.UpdateTargetUnitCommandEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid),
	FOREIGN KEY (ability) REFERENCES datapack.ability(iid),
	FOREIGN KEY (target) REFERENCES datapack.unit_type(iid)
);

create table events.UnitTypeChangeEvent
(
	iid				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	unit_id_index           	integer,
	unit_id_recycle         	integer,
	unit_id         		integer,
	unit            		integer,
	unit_type_name          	varchar(100),
	PRIMARY KEY (iid),
	FOREIGN KEY (unit) REFERENCES datapack.unit_type(iid)
);

create table events.UnitDiedEvent
(
	iid				serial,
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
	PRIMARY KEY (iid),
	FOREIGN KEY (killer) REFERENCES replay.player(iid),
	FOREIGN KEY (killing_player) REFERENCES replay.player(iid),
	FOREIGN KEY (unit) REFERENCES datapack.unit_type(iid),
	FOREIGN KEY (killing_unit) REFERENCES datapack.unit_type(iid)
);

create table events.UnitPositionsEvent
(
	iid				serial,
	frame           		integer,
	second          		integer,
	name            		varchar(100),
	first_unit_index                integer,
	-- -- items           		<class 'list'>,
	-- -- units           		<class 'dict'>,
	-- -- positions               	<class 'list'>,
	PRIMARY KEY (iid)
);

create table events.PlayerLeaveEvent
(
	iid				serial,
	pid             		integer,
	player          		integer,
	frame           		integer,
	second          		integer,
	is_local                	boolean,
	name            		varchar(100),
	-- -- data            		<class 'dict'>,
	PRIMARY KEY (iid),
	FOREIGN KEY (player) REFERENCES replay.player(iid)
);
