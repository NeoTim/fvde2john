/*
 * Definitions for libfvde
 *
 * Copyright (C) 2011-2016, Omar Choudary <choudary.omar@gmail.com>
 *                          Joachim Metz <joachim.metz@gmail.com>
 *
 * Refer to AUTHORS for acknowledgements.
 *
 * This software is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this software.  If not, see <http://www.gnu.org/licenses/>.
 */

#if !defined( _LIBFVDE_DEFINITIONS_H )
#define _LIBFVDE_DEFINITIONS_H

#include <libfvde/types.h>

#define LIBFVDE_VERSION					20160918

/* The version string
 */
#define LIBFVDE_VERSION_STRING				"20160918"

/* The file access
 * bit 1        set to 1 for read access
 * bit 2        set to 1 for write access
 * bit 3-8      not used
 */
enum LIBFVDE_ACCESS_FLAGS
{
	LIBFVDE_ACCESS_FLAG_READ			= 0x01,
/* Reserved: not supported yet */
	LIBFVDE_ACCESS_FLAG_WRITE			= 0x02
};

/* The file access macros
 */
#define LIBFVDE_OPEN_READ				( LIBFVDE_ACCESS_FLAG_READ )
/* Reserved: not supported yet */
#define LIBFVDE_OPEN_WRITE				( LIBFVDE_ACCESS_FLAG_WRITE )
/* Reserved: not supported yet */
#define LIBFVDE_OPEN_READ_WRITE				( LIBFVDE_ACCESS_FLAG_READ | LIBFVDE_ACCESS_FLAG_WRITE )

/* The encryption methods
 */
enum LIBFVDE_ENCRYPTION_METHODS
{
	LIBFVDE_ENCRYPTION_METHOD_AES_XTS		= 2
};

#endif

