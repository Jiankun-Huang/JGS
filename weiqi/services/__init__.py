# weiqi.gs
# Copyright (C) 2016 Michael Bitzi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .base import BaseService, ServiceError
from .rating import RatingService
from .rooms import RoomService
from .users import UserService
from .correspondence import CorrespondenceService
from .games import GameService
from .connection import ConnectionService
from .play import PlayService
from .settings import SettingsService
from .dashboard import DashboardService
from .search import SearchService

from .executor import execute_service
